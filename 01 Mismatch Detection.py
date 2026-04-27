"""

TL; DR:
Checks whether each account's assigned sales region actually matches its billing country,
using a hardcoded country → region map (e.g. UK/Ireland → UKI, Nordics → EMEANorth).
Prints a count of mismatches and a sample table to the terminal.


Prerequisites:
- Python 3.x installed (https://www.python.org/downloads/)
- Pandas installed (run `pip install pandas` in Command Prompt). How to - Open Command Prompt like in Step 2 below, and enter run`pip install pandas
- Your CSV file placed in the same folder as this .py file or provide full file paths

This programme compares the 'Account Owner Region' with the expected region
based on the 'Billing Country', identifies mismatches, and displays a summary
of rows where the assigned region does not match the expected one.

To run this programme (On Windows):

1. On line 38, copy and paste the file path of the CSV file
(make sure the file is in the same folder as this .py file).
2. Go to Command Prompt (type it into the Windows search bar) or press the Windows key + R and type `cmd`.
3. Enter: cd <file path of the folder (not the file) where this .py file is located>
4. To run the programme, type: python main.py on Command Prompt
"""

import pandas as pd

# Country to Account Owner Region mapping
country_to_region = {
    'united kingdom': 'UKI',
    'ireland': 'UKI',
    'france': 'FR',
    'germany': 'DE',
    'finland': 'EMEANorth',
    'norway': 'EMEANorth',
    'sweden': 'EMEANorth',
    'netherlands': 'EMEANorth',
    'belgium': 'EMEANorth',
    'luxembourg': 'EMEANorth',
    'spain': 'EMEASouth',
    'portugal': 'EMEASouth',
    'italy': 'EMEASouth',
    'israel': 'EMEASouth',
    'meta': 'EMEASouth',
    'eastern europe': 'EMEASouth',
}

# Load the data
df = pd.read_csv(r"copy and paste the file path of the csv that's in the same folder as this .py file")

# Neaten strings
df['Account Owner Region'] = df['Account Owner Region'].astype(str).str.strip()
df['Billing Country'] = df['Billing Country'].astype(str).str.strip().str.lower()

# Map billing country to expected region
df['Expected Region'] = df['Billing Country'].map(country_to_region)

# Only consider rows where Expected Region is known
filtered = df[df['Expected Region'].notna()]

# Find real mismatches
mismatches = filtered[filtered['Account Owner Region'] != filtered['Expected Region']]

# Print data
print(f"Total rows with mapped countries: {len(filtered)}")
print(f"Total real mismatches: {len(mismatches)}")
print("\nSample mismatches:")
print(mismatches[['Account ID', 'Account Owner Region', 'Billing Country', 'Expected Region']].head(10))

