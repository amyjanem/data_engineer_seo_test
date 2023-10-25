import pandas as pd
import numpy as np
import re
import csv

print('starting code...')

regex = r"(\d{8})\s+(\d{12})\s+(\d{8})\s+(\w+ \w+)\s+(\d{6})\s+(\w+)\s+(\w+)\s+(\w+)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)"

def parse_row(data):
    """Parses a single row of data and returns a dictionary of the parsed fields."""

    match = regex.match(data)
    if match is None:
        return None

    return {
        'company_number': match.group(1),
        'person_number': match.group(2),
        'date_appointment': match.group(3),
        'postcode': match.group(4),
        'date_of_birth': match.group(5),
        'title': match.group(6),
        'first_name': match.group(7),
        'last_name': match.group(8),
        'honours': match.group(9),
        'care_of': match.group(10),
        'po_box': match.group(11),
        'first_line_address': match.group(12), 
        'second_line_address': match.group(13), 
        'town': match.group(14),
        'county': match.group(15),
        'country': match.group(16)
        }
  
parsed_data = []

print('reading txt file...')

with open('officer_snapshot.txt', 'r') as f:
    for line in f:
        parsed_row = parse_row(line)
        if parsed_row is not None:
            parsed_data.append(parsed_row)
            
with open('parsed_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['company_number', 'person_number', 'date_appointment', 'postcode', 'date_of_birth', 'title', 'first_name', 'last_name', 'honours', 'care_of', 'po_box', 'first_line_address', 'second_line_address', 'town', 'county', 'country'])
    for row in parsed_data:
        writer.writerow([row['company_number'], row['person_number'], row['date_appointment'], row['postcode'], row['date_of_birth'], row['title'], row['first_name'], row['last_name'], row['honours'], row['care_of'], row['po_box'], row['first_line_address'], row['second_line_address'], row['town'], row['county'], row['country']])