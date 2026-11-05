# F1 Telemetry Data Analysis

Python-based data extraction and performance analysis tool utilizing the official FastF1 API. Developed for motorsport engineering portfolio applications.

## Overview
This project automates the extraction, processing, and visualization of Formula 1 telemetry data. It evaluates vehicle dynamics during competitive sessions by analyzing critical parameters, including speed profiles, throttle application, and braking inputs relative to circuit distance.

## Key Features
- **Automated Data Retrieval:** Fetches official session timing, lap data, and raw telemetry via the FastF1 API.
- **Local Caching:** Implements local caching to optimize execution time and prevent redundant API queries.
- **Telemetry Visualizer:** Generates multi-subplot performance figures:
  - **Speed Trace:** Velocity (Km/h) versus track distance (m).
  - **Driver Controls:** Throttle percentage and binary brake status.
- **Configurability:** Easily scalable for any driver, season, Grand Prix, and session type (Practice, Qualifying, Race).

## Tech Stack
- **Language:** Python 3.11
- **Libraries:** 
  - `fastf1` (Telemetry & timing data)
  - `matplotlib` (Engineering data visualization)
  - `pandas`, `numpy` (Data manipulation)

## Installation & Setup

> **NOTE:** Recent updates to the FastF1 API require an official Formula 1 account to fetch live/session data. If you don't have one, create a free account at [formula1.com](https://www.formula1.com) before running the script. The first time you execute the code, the terminal will prompt you to enter your F1 account email and password.

1. Clone the repository:
   git clone https://github.com/YOUR_USERNAME/F1-Telemetry-Data-Analysis.git
   cd F1-Telemetry-Data-Analysis

2. Install dependencies:
   pip install -r requirements.txt

3. Create the cache directory:
   mkdir cache

## Usage

Execute the main script to analyze a specific driver's fastest lap (e.g., Max Verstappen, 2023 Bahrain Grand Prix):
python src/telemetry_plot.py

## Roadmap
- [ ] Multi-driver telemetry comparison (teammate delta analysis).
- [ ] Corner-by-corner minimum speed and braking point detection.
- [ ] Automated export of performance metrics to structured reports.