#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import csv
import tkinter as tk
from tkinter import filedialog

# Create the main window
root = tk.Tk()
root.withdraw()

# Prompt the user to select a folder
folder_path = filedialog.askdirectory(title="Select a Folder")

# Check if a folder was selected
if not folder_path:
    print("No folder selected. Exiting...")
    exit()

# Output CSV file name
output_file = "combined.csv"

# Initialize the combined data list
combined_data = []

# Iterate over the CSV files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(folder_path, filename)

        # Read each CSV file
        with open(file_path, "r") as file:
            csv_reader = csv.reader(file)

            # Iterate over the rows in the CSV file
            for row in csv_reader:
                # Convert the first column value to float and divide by 1000000
                row[0] = float(row[0]) / 1000000

                # Append the modified row to the combined data list
                combined_data.append(row)

# Write the combined data to the output CSV file
output_path = os.path.join(folder_path, output_file)
with open(output_path, "w", newline="") as file:
    csv_writer = csv.writer(file)

    # Write the rows to the output CSV file
    csv_writer.writerows(combined_data)

print(f"CSV files combined and modified successfully. Output file: {output_path}")

# Open the folder containing the output CSV file
folder_dir = os.path.dirname(output_path)
os.startfile(folder_dir)


# In[ ]:




