"""Render the public GitHub contribution calendar and streaks as one SVG."""
import re
import sys
from collections import defaultdict
from datetime import date, timedelta
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen


class Calendar(HTMLParser):
    def __init__(self):
        super().__init__()
        self.levels = {}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "td" and "data-date" in attrs and "data-level" in attrs:
            day = date.fromisoformat(attrs["data-date"])
            self.levels[day] = int(attrs["data-level"])


def streak(periods, current, step):
    # The current period can still receive a contribution.
    if not periods.get(current):
        current -= step
    length = 0
    while periods.get(current):
        length += 1
        current -= step
    return length


def render(levels):
    today = max(levels)
    first = min(levels)
    week = timedelta(days=7)
    day_step = timedelta(days=1)
    sunday = lambda day: day - timedelta(days=(day.weekday() + 1) % 7)
    start = sunday(first)
    weekly = defaultdict(bool)
    colors = ("#222b38", "#0e4429", "#006d32", "#26a641", "#56d364")
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="960" height="215" viewBox="0 0 960 215" role="img" aria-labelledby="title">',
        '<title id="title">GitHub contribution calendar and current streaks</title>',
        '<rect width="960" height="215" rx="16" fill="#0d1117"/>',
        '<g font-family="system-ui,sans-serif" fill="#e6edf3">',
        '<text x="28" y="34" font-size="19" font-weight="600">GitHub contributions</text>',
    ]
    month = None
    for day, level in sorted(levels.items()):
        x = 28 + ((day - start).days // 7) * 17
        y = 63 + ((day - start).days % 7) * 15
        weekly[sunday(day)] |= level > 0
        if (day.year, day.month) != month and (day - first).days > 6:
            parts.append(f'<text x="{x}" y="55" font-size="10" fill="#9ca9b8">{day:%b}</text>')
            month = (day.year, day.month)
        elif month is None:
            month = (day.year, day.month)
        parts.append(f'<rect x="{x}" y="{y}" width="12" height="12" rx="2" fill="{colors[level]}"></rect>')
    daily = streak(levels, today, day_step)
    weeks = streak(weekly, sunday(today), week)
    parts.append(f'<text x="28" y="192" font-size="13">Current daily streak: {daily} days · Current weekly streak: {weeks} weeks</text>')
    parts.append(f'<text x="932" y="192" text-anchor="end" fill="#9ca9b8" font-size="12">Through {today:%d %b %Y}</text>')
    return "\n".join(parts + ["</g></svg>", ""])


if __name__ == "__main__":
    login = sys.argv[1]
    if not re.fullmatch(r"[A-Za-z0-9-]+", login):
        raise SystemExit("Invalid GitHub login")
    request = Request(f"https://github.com/users/{login}/contributions", headers={"User-Agent": "GitHub profile activity renderer"})
    with urlopen(request, timeout=25) as response:
        html = response.read().decode()
    calendar = Calendar()
    calendar.feed(html)
    if not 300 <= len(calendar.levels) <= 380:
        raise SystemExit("GitHub did not return a complete contribution calendar")
    Path(sys.argv[2]).write_text(render(calendar.levels), encoding="utf-8")
