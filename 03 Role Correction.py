"""

TL; DR:
The only script that actually writes a file. Reads the CSV, finds rows flagged as "Mismatch",
flips the rep role (SDR ↔ Comm Rep), and saves a corrected CSV to a location you specify.

Prerequisites:
- Python 3.x installed (https://www.python.org/downloads/)
- Pandas installed (run `pip install pandas` in Command Prompt). How To - Open Command Prompt like in Step 2 below, and enter run`pip install pandas
- Your CSV file placed in the same folder as this .py or provide full file paths

This script reads a CSV file containing account assignments,
identifies mismatches in the 'Support SDR' role, and flips the role
(e.g. SDR → Comm Rep or vice versa) where mismatches are found.
The amended dataset is then saved as a new CSV file.

To run this programme (on Windows):

1. On line 14, copy and paste the file path of the CSV file (ensure it's in the same folder as this .py file).
2. On line 33, copy and paste the file path of the folder where you want the amended data file to be saved.
3. Open Command Prompt (type it into the Windows search bar) or press the Windows key + R and type `cmd`.
4. Type: cd <path to the folder where this .py file is located> and press Enter.
5. To run the programme, type: python main.py
"""
import pandas as pd

# Pass through the CSV file
df = pd.read_csv(r"copy and paste the file path of CSV here + make sure the file is in the same folder as this .py file")

# Neaten values
df['Support SDR'] = df['Support SDR'].astype(str).str.strip().str.lower()
df['Match/Mismatch'] = df['Match/Mismatch'].astype(str).str.strip().str.lower()

# Define role flipping function
def flip_role(role):
    if role == 'sdr':
        return 'comm rep'
    elif role == 'comm rep':
        return 'sdr'
    else:
        return role  # Leave unchanged if not recognised

# Flip role where it's a mismatch
df.loc[df['Match/Mismatch'] == 'mismatch', 'Support SDR'] = df.loc[df['Match/Mismatch'] == 'mismatch', 'Support SDR'].apply(flip_role)

# Where to save the updated dataset
df.to_csv(r"Copy and paste the file path of folder, where you want the amended data set to be saved", index=False)
