"""

TL; DR:
Finds accounts with 500+ employees that aren't assigned to an SDR.
Groups the gaps by region so sales ops can see exactly where coverage is lacking — useful for headcount planning.

Prerequisites:
- Python 3.x installed (https://www.python.org/downloads/)
- Pandas installed (run `pip install pandas` in Command Prompt). How to - Open Command Prompt like in Step 2 below, and enter run`pip install pandas
- Your CSV file placed in the same folder as this .py file or provide full file paths

This script analyses a dataset of company accounts to identify large accounts (500+ employees)
that are not assigned to SDRs, then summarises the distribution of those mismatches by region
and displays a sample of affected accounts.

To run this programme(on Windows):

1. On line 16, paste the file path of the CSV file.
2. Open Command Prompt (search for "cmd" or press Windows + R and type `cmd`).
3. Type: cd <folder path where this .py file is located>
4. Run the script by typing: python main.py
"""

import pandas as pd

# Load the CSV
df = pd.read_csv(r"copy and paste the file path of the csv that's in the same folder as this .py file")

# Print column names to verify what exists
print("Column Names in CSV:")
print(df.columns.tolist())

# Normalise key fields
df['Account Owner Region'] = df['Account Owner Region'].astype(str).str.strip()
df['Billing Country'] = df['Billing Country'].astype(str).str.strip().str.lower()
df['Account Name'] = df['Account Name'].astype(str).str.strip().str.lower()
df['Industry'] = df['Industry'].astype(str).str.strip().str.lower()
df['Support SDR'] = df['Support SDR'].astype(str).str.strip().str.lower()

# Use 'Support SDR' as proxy for Rep Type
df['Rep Type'] = df['Support SDR']

# Filter accounts with 500+ employees
df = df[df['Employees'].notna()]
large_accounts = df[df['Employees'] >= 500]

# Filter accounts NOT assigned to SDRs
non_sdr_large_accounts = large_accounts[~large_accounts['Rep Type'].isin(['yes', 'y', 'true'])]

# Group by region to find where mismatches happen most
summary = non_sdr_large_accounts.groupby('Account Owner Region').size().reset_index(name='Non-SDR Large Accounts')

# Final output
print(f"\n Large Accounts (500+ Employees) NOT Assigned to SDRs: {len(non_sdr_large_accounts)} accounts")

print("\n Mismatches by Region:")
print(summary.sort_values('Non-SDR Large Accounts', ascending=False))

print("\n Sample Mismatched Accounts:")
print(non_sdr_large_accounts[['Account Name', 'Employees', 'Billing Country', 'Account Owner Region', 'Rep Type']].head(10))
