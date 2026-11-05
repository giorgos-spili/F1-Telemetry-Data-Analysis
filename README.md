# F1 Telemetry Data Analysis

Python-based data extraction and performance analysis tool utilizing the official FastF1 API. Developed for motorsport engineering portfolio applications.

## Overview
This project automates the extraction, processing, and visualization of Formula 1 telemetry data. It evaluates vehicle dynamics during competitive sessions by analyzing critical parameters, including speed profiles, throttle application, and braking inputs relative to circuit distance.


## Installation & Setup

> **NOTE:** Recent updates to the FastF1 API require an official Formula 1 account to fetch live/session data. If you don't have one, create a free account at formula1.com before running the script. The first time you execute the code, the terminal will prompt you to enter your F1 account email and password.

1. Clone the repository:
   git clone [https://github.com/giorgos-spili/F1-Telemetry-Data-Analysis.git](https://github.com/giorgos-spili/F1-Telemetry-Data-Analysis.git)
   cd F1-Telemetry-Data-Analysis

2. Install dependencies:
   pip install -r requirements.txt

3. Create the cache directory:
   mkdir cache

## Usage

Execute the main script to analyze a specific driver's fastest lap (e.g., Max Verstappen, 2023 Bahrain Grand Prix):
python src/telemetry_plot.py

