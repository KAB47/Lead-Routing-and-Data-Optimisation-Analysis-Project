# Lead Routing and Data Optimisation — Snowflake Panel Presentation

A multi-tool data analysis project auditing a Snowflake EMEA CRM dataset of ~22,857 accounts to diagnose broken SDR and Comm Rep lead routing, quantify the damage, and propose fixes — using Excel, Power BI, and Python.

## TL;DR

Auditing ~22,000 Snowflake EMEA CRM accounts to find why SDRs and Comm Reps were receiving wrong leads — using Excel to flag mismatches, Power BI to visualise them, and Python to automate corrections.

**Main Insights Found/Outcomes**
1. 24% of all leads (4,446 accounts) are incorrectly routed. 
2. Germany has the highest mismatch rate at 58%. 
3. 70% of mismatches involve enterprise accounts (500+ employees). 
4. 3,796 large accounts have zero SDR coverage. 
5. 65% of all rows have billing country misaligned with account owner region. 
6. Some Comm Reps are managing enterprise accounts they shouldn't own, and certain SDRs are under-assigned relative to expected pipeline volume.

## Background

**The business rule:** SDRs support enterprise accounts with 500+ employees. Comm Reps handle commercial accounts with fewer than 500 employees.

**The brief:** Review the dataset, identify what is causing leads to be routed incorrectly to SDR and Comm Rep teams, and propose solutions.

## Root Causes Identified

| # | Issue | Description |
|---|-------|-------------|
| 1a | Mismatched rep type | Accounts with 500+ employees routed to Comm Reps instead of SDRs |
| 1b | Missing SDR assignment | Expected SDR routing not applied to accounts at all |
| 2 | Region/country misalignment | Billing Country does not align with Account Owner Region logic |
| 3 | Inconsistent size-based routing | Same company size routed differently across similar regions |

## Key Results

- **22,857** total accounts across EMEA
- **17,462** correctly routed (Match)
- **4,446** incorrectly routed (Mismatch) — **24% of all leads**
- **949** unassigned/unknown routing
- **Germany (DE)** — highest mismatch rate at **58%**
- **EMEACommercial** — lowest mismatch rate at **9%** (highest match rate 91%)
- **3,796** large accounts (500+ employees) with no SDR coverage
  - DE accounts for **1,929** of these (51% of the problem)
- **70%** of all mismatches involve enterprise (500+) accounts
- **65%** of all rows have billing country and account owner region misaligned

## Tools & Stack

- **Microsoft Excel** — IF/nested logic formulas, pivot tables, bar charts, match/mismatch flagging
- **Power BI** — interactive dashboard with KPI cards, stacked bar charts, donut charts, and cross-filtered views by region, company size, and industry
- **Python 3 + pandas** — automated data audit and correction scripts
- **Adobe InDesign** — 13-slide panel presentation built to Snowflake brand standards
- **Dataset** — ~22,857 CRM account records across EMEA regions

## Analysis Breakdown

### Excel — Mismatch Detection
An `Expected SDR Assignment` column was created using an IF formula based on employee count:
```
=IF(I2="", "Unknown", IF(I2>=500, "SDR", "Comm Rep"))
```
A second column then compared this against the actual `Support SDR` field:
```
=IF(L2=M2, "Match", "Mismatch")
```
A pivot table summarised mismatch rates by region, revealing DE at 58% and EMEACommercial at 9%.

### Power BI — Dashboard Insights
An interactive dashboard was built surfacing:
- Total leads, correct vs. incorrect routing, and unassigned counts as KPI cards
- Support SDR vs. Expected SDR Assignment stacked bar chart
- Mismatch by company size (Enterprise 500+ vs. Commercial <500)
- Account size segment donut (79.41% Commercial, 16.44% Enterprise)
- Billing country distribution bar chart
- Industry breakdown pie chart (Software B2B leads at 26.53%)

### Python — Code 1: Billing Country vs. Account Owner Region
Uses a country-to-region dictionary to check whether each account's billing country aligns with its assigned region. 87% of rows had a mappable country, of which 74% were misaligned — meaning **65% of all rows** fail region/country logic.

### Python — Code 2: Large Accounts Without SDR Coverage
Filters accounts with 500+ employees not assigned to SDRs and groups by region. **3,796 large accounts** lack SDR coverage, with DE (1,929) and EMEACommercial (727) most affected.

### Python — Code 3: Automated Role Correction
Reads the mismatch-flagged CSV, flips the rep role for all rows marked `Mismatch` (SDR ↔ Comm Rep), and saves a corrected output CSV — fully automating the remediation.

## Recommendations

1. **Automate lead routing logic** — use employee count + country rules in Salesforce to assign SDR/Comm Rep automatically, removing manual error
2. **Fix region definitions in CRM** — use formulas to flag when an account is 500+ employees but routed to Comm Rep
3. **Add data validation rules** — when selecting billing country, force the corresponding Account Owner Region (e.g. DE = Germany only)
4. **Use an API** — if routing runs through a legacy system, offload/filter through a modern API to apply correct logic

## Prerequisites

- Python 3.x — [python.org/downloads](https://www.python.org/downloads/)
- pandas library

```
pip install pandas
```

## Running the Python Scripts

1. Place `main.py` and your CSV file in the same folder
2. Open the script and paste your CSV file path on the indicated line
3. Open Command Prompt and navigate to the folder:
```
cd <path to folder>
```
4. Run the script:
```
python main.py
```

> **Note:** Code 3 is the only script that produces an output file. Codes 1 and 2 print results to the terminal. The dataset CSV used during development is included in each code folder.

## Project Structure

```
Project File Overview
├── Lead Routing and Data Optimisation Panel Presentation.pdf # Adobe InDesign (PowerPoint) Presentation of the whole project (Please download, as it is not viewable on Github directly)
├── Dataset.csv
├── Dataset After Put Through 'Role Correction Code Base.csv
├── 01 Mismatch Detection.py # Region vs. billing country audit
├── 02 SDR Coverage Audit.py # Large account SDR coverage audit
├── 03 Role Correction.py # Automated rep role correction
├── README.md                           

```
