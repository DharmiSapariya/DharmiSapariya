name: GitHub-Profile-Summary-Cards

on:
  schedule:
    - cron: "0 0 * * *"   # once a day at 00:00 UTC
  workflow_dispatch:       # lets you run it by hand from the Actions tab

permissions:
  contents: write          # needed to push the generated SVGs

jobs:
  build:
    runs-on: ubuntu-latest
    name: generate-github-profile-summary-cards
    steps:
      - uses: actions/checkout@v4
      - uses: vn7n24fzkq/github-profile-summary-cards@release
        env:
          # Use a personal access token (secret named SUMMARY_GITHUB_TOKEN).
          # The default GITHUB_TOKEN often fails with
          # "Resource not accessible by integration" or skips some cards.
          GITHUB_TOKEN: ${{ secrets.SUMMARY_GITHUB_TOKEN }}
        with:
          USERNAME: ${{ github.repository_owner }}
          BRANCH_NAME: "main"
          UTC_OFFSET: 5   # IST is UTC+5:30; the action takes whole hours
