import pandas as pd
import numpy as np
import re
import csv

with open('officer_snapshot.txt', "r") as f:
    # Read all of the text from the file
    text = f.read()

print(text) # Print the text to the terminal

# officer_df = pd.DataFrame(text)
# print(officer_df)

# regex = r'(\d{8})\s+(\d{12})\s+(\d{8})\s+(\w+ \w+)\s+(\d{6})\s+(\w+)\s+(\w+)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)'