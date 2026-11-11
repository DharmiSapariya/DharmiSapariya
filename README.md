<div align="center">

<img src="./banner.svg" width="100%" alt="Dharmi Sapariya: AI-backed software, from data pipelines to hardware" />

<br/>

[![GitHub](https://img.shields.io/badge/GitHub-DharmiSapariya-161b22?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DharmiSapariya)
[![Followers](https://img.shields.io/github/followers/DharmiSapariya?style=for-the-badge&logo=github&label=Followers&color=58a6ff&labelColor=161b22)](https://github.com/DharmiSapariya?tab=followers)
[![Profile views](https://komarev.com/ghpvc/?username=DharmiSapariya&style=for-the-badge&label=Profile+views&color=58a6ff&labelColor=161b22)](https://github.com/DharmiSapariya)
[![Last commit](https://img.shields.io/github/last-commit/DharmiSapariya/NextSkill?style=for-the-badge&logo=git&logoColor=white&label=Last+commit&color=58a6ff&labelColor=161b22)](https://github.com/DharmiSapariya?tab=repositories)

**[Selected work](#selected-work)** · **[Architecture](#how-two-of-them-work)** · **[Activity](#activity)** · **[git-koi](#git-koi)** · **[Learning](#certifications-and-learning)** · **[Stack](#tech-stack)**

</div>

<!--
  Add contact badges here, for example:
  [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/YOUR-HANDLE)
  [![Email](https://img.shields.io/badge/Email-161b22?style=for-the-badge&logo=gmail&logoColor=white)](mailto:YOUR-EMAIL)
-->

<img src="./metrics.svg" width="100%" alt="Selected numbers: 156 tests, 30+ API endpoints, 92.35% blocking recall, 44 tests" />

## Focus

| Area | What I do | Evidence |
|---|---|---|
| **Data & ML** | Ingestion, NLP, detection and matching pipelines | Skill extraction in NextSkill, deepfake scoring in Kavach, entity resolution at 92.35% blocking recall |
| **Full-stack** | APIs, dashboards and AI features behind a secure backend | React, Node, FastAPI and PostgreSQL apps with CI, Docker and test suites |
| **Hardware + software** | Sensors, control loops and live visualisation | Raspberry Pi and Arduino projects with a 3D digital twin and sensor fusion |

## Selected work

<table>
<tr>
<td width="50%" valign="top">

### [NextSkill](https://github.com/DharmiSapariya/NextSkill)
Career intelligence for the tech job market, built for individuals instead of enterprises. Job postings from two sources go into PostgreSQL, NLP extracts the skills, and the dashboard recommends what to learn next. Every number traces back to real postings.

**30+ API endpoints · 156 tests**

[![NextSkill CI status on main](https://github.com/DharmiSapariya/NextSkill/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/DharmiSapariya/NextSkill/actions/workflows/ci.yml?query=branch%3Amain)

`Python` `FastAPI` `PostgreSQL` `Redis` `Docker` `spaCy` `Streamlit`

</td>
<td width="50%" valign="top">

### [Kavach](https://github.com/DharmiSapariya/Kavach)
Free deepfake detection for women in India. A 4-signal pipeline scores any image or video, then helps the user act: a pre-filled FIR draft, platform takedown reports, and a WhatsApp bot for quick checks.

**4-signal detection · FIR draft · WhatsApp bot**

`React` `Tailwind` `FastAPI` `PyTorch` `OpenCV`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [WalletWise](https://github.com/DharmiSapariya/WalletWise)
Full-stack personal finance dashboard with an AI coach that reads the user's real transactions. Server-side analytics (trend regression, anomaly detection, Monte-Carlo budget forecasting), and the Claude API runs on the backend so keys never reach the browser.

**44 automated tests · Docker Compose**

[![WalletWise CI status on main](https://github.com/DharmiSapariya/WalletWise/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/DharmiSapariya/WalletWise/actions/workflows/ci.yml?query=branch%3Amain)

`React` `Node.js` `Express` `PostgreSQL` `Claude API`

</td>
<td width="50%" valign="top">

### [NeuraVapor](https://github.com/DharmiSapariya/NeuraVapor)
Engineering Clinics capstone: a closed-loop prototype that turns data-center waste heat into distilled water using membrane distillation, with noise-adaptive control and a live 3D digital twin in the browser. Built on about INR 6,000 to 7,000.

**Closed-loop control · live 3D twin**

`Raspberry Pi` `Python` `Three.js` `Sensors`

</td>
</tr>
<tr>
<td colspan="2" valign="top">

### [Amazon ML Challenge 2026: Business Entity Resolution](https://github.com/DharmiSapariya/Amazom_ML_Challenge_2026)
Two-stage pipeline for matching noisy business records: high-recall candidate generation, then hard-negative matching. I built the data engineering and blocking stage, which reached **92.35% blocking recall** on the validation sample, up from about 24% for the first baseline.

`Python` `Pandas` `RapidFuzz` `scikit-learn` `LightGBM`

</td>
</tr>
</table>

<details>
<summary><b>More projects</b></summary>
<br/>

| Project | What it is | Stack |
|---|---|---|
| [**SafeBite**](https://github.com/Jasmine0987/safebite) | Allergen-aware food label scanner: OCR, personal diet profile, safe / flagged / unclear verdicts, and swap suggestions | `FastAPI` `OCR` `JavaScript` |
| [**ResourceRX**](https://github.com/DharmiSapariya/ResourceRX) | Peer-to-peer medical equipment sharing network with clinic, owner, technician and logistics portals and a local Ollama assistant | `React` `Vite` `Node.js` `Ollama` |
| [**BorderEye**](https://github.com/DharmiSapariya/BorderEye) | Arduino intrusion detection that fuses ultrasonic, metal, gas and temperature sensors with Bluetooth alerts | `Arduino` `C++` |

</details>

### How two of them work

<details>
<summary><b>NextSkill:</b> from job postings to a learning recommendation</summary>

```mermaid
flowchart LR
    A["Job postings<br/>2 sources"] --> B[("PostgreSQL")]
    B --> C["NLP skill extraction<br/>spaCy"]
    C --> D["FastAPI<br/>30+ endpoints"]
    D --> E["Streamlit dashboard"]
    E --> F["What to learn next"]
```

</details>

<details>
<summary><b>Kavach:</b> from a suspicious file to action</summary>

```mermaid
flowchart LR
    A["Image or video<br/>web app or WhatsApp bot"] --> B["4-signal<br/>detection pipeline"]
    B --> C{"Score"}
    C --> D["Pre-filled FIR draft"]
    C --> E["Platform takedown report"]
```

</details>

## Activity

<p align="center">
  <img src="https://streak-stats.demolab.com?user=DharmiSapariya&hide_border=true&border_radius=10&background=0D1117&stroke=30363D&ring=58A6FF&fire=F78166&currStreakNum=F0F6FC&sideNums=F0F6FC&currStreakLabel=58A6FF&sideLabels=8B949E&dates=6E7681" width="49%" alt="Daily contribution streak" />
  <img src="https://streak-stats.demolab.com?user=DharmiSapariya&mode=weekly&hide_border=true&border_radius=10&background=0D1117&stroke=30363D&ring=BC8CFF&fire=F78166&currStreakNum=F0F6FC&sideNums=F0F6FC&currStreakLabel=BC8CFF&sideLabels=8B949E&dates=6E7681" width="49%" alt="Weekly contribution streak" />
</p>
<p align="center"><sub>Daily streak (left) and weekly streak (right)</sub></p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=DharmiSapariya&theme=github-dark&hide_border=true&bg_color=0d1117&color=58a6ff&line=58a6ff&point=f0f6fc" width="98%" alt="Contribution activity graph" />
</p>

<p align="center">
  <img src="./profile-summary-card-output/tokyonight/3-stats.svg" width="49%" alt="GitHub stats" />
  <img src="./profile-summary-card-output/tokyonight/2-most-commit-language.svg" width="49%" alt="Most used languages" />
</p>
<p align="center">
  <img src="./profile-summary-card-output/tokyonight/1-repos-per-language.svg" width="49%" alt="Repos per language" />
  <img src="./profile-summary-card-output/tokyonight/4-productive-time.svg" width="49%" alt="Productive time" />
</p>
<p align="center"><sub><a href="https://github.com/DharmiSapariya/DharmiSapariya/actions/workflows/profile-summary-cards.yml">Profile card refresh history</a></sub></p>

## git-koi

<table>
<tr>
<td width="290" align="center" valign="middle">
  <img src="./koi/koi.gif" width="256" alt="My git-koi, redrawn nightly from my GitHub activity" />
  <br/><sub>My koi, redrawn nightly (00:20 UTC)</sub>
</td>
<td valign="top">

**[git-koi](https://github.com/yalongwastaken/git-koi)** turns a GitHub account's public activity into a unique pixel-art koi, so the profile shows a living summary of the work instead of only counters.

| Signal | What it changes on the koi |
|---|---|
| Languages used | Colours |
| Total contributions | Growth stage |
| Weekly streaks | Fins, colour vibrancy and a glimmer for long records |
| Yesterday's activity | Movement: cruise, dart, surface-feed, rest |

**Automated:** a GitHub Action reads public data with the built-in token and commits a new looping GIF each night. **Six bodies:** white, black, asagi, tea, gold, platinum (mine is gold).

<sub>Set it up from the <a href="https://github.com/yalongwastaken/git-koi/blob/main/docs/getting-started.md">getting-started guide</a>. Created by <a href="https://github.com/yalongwastaken">@yalongwastaken</a>.</sub>

</td>
</tr>
</table>

## Certifications and Learning

| | |
|---|---|
| [**OCI Generative AI Professional**](https://github.com/DharmiSapariya/Oracle-Cloud-Infrastructure-Generative-AI-Professional-Certification) | Labs, runbooks and 300+ practice questions covering LLMs, RAG with LangChain and Oracle 23ai, and GenAI Agents |
| [**JPMorgan Chase Quantitative Research**](https://github.com/DharmiSapariya/jpmc_quant_research_certification) | Forage simulation: natural gas price estimation and contract pricing, loan default prediction, FICO score bucketing |
| [**Kaggle: Intro to Machine Learning**](https://github.com/DharmiSapariya/Kaggle-Intro-to-Machine-Learning) | Notes and notebooks on decision trees and random forests |
| [**SQL practice**](https://github.com/DharmiSapariya/SQL-LeetCode) | LeetCode SQL solutions, updated as I go |

## Tech Stack

| | |
|---|---|
| **Languages** | ![](https://skillicons.dev/icons?i=py,js,html,css,cpp&theme=dark) |
| **Frameworks & Libraries** | ![](https://skillicons.dev/icons?i=fastapi,flask,react,tailwind,nodejs,express&theme=dark) |
| **AI & ML** | ![](https://skillicons.dev/icons?i=pytorch,opencv,numpy&theme=dark) `scikit-learn` `spaCy` `LangChain` `Transformers` `MediaPipe` |
| **Data & Infra** | ![](https://skillicons.dev/icons?i=postgres,redis,docker&theme=dark) |
| **Hardware** | ![](https://skillicons.dev/icons?i=arduino,raspberrypi&theme=dark) |
| **Design** | ![](https://skillicons.dev/icons?i=figma&theme=dark) |
| **IDEs & Tools** | ![](https://skillicons.dev/icons?i=vscode,pycharm,idea,git,github&theme=dark) |

<div align="center"><sub>Stats refresh automatically · koi drawn nightly by <a href="https://github.com/yalongwastaken/git-koi">git-koi</a></sub></div>
