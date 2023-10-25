import pandas as pd
#import regex 

# df_officer_data = pd.read_csv('officer_snapshot.txt', sep=',', header=None, engine = 'python')

# display(df__officer_data)
# 88958775556806630001    20190429    CR4 1XW 197404MR<INDIGO<VANVU<<<<3 SHROPSHIRE CLOSE<<MITCHAM<<ENGLAND
#regex = r'(\d{8})+(\d{12})\s*+(\d{8})\s*+(\w+ \w+)\s*+(\d{6})\s*+([A-Z]+)<+([A-Z]+)<+([A-Z]+)<+([0-9]+)\s*+([A-Z])\s*+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)'
regex = r'(\d{8})\s+(\d{12})\s+(\d{8})\s+(\w+ \w+)\s+(\d{8})\s+([A-Z]+)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)'

pd.set_option('display.max_columns', None) # You can use this setting display all the columns in your dataframe
flights_df = pd.read_csv("officer_snapshot.txt", sep=',') 
flights_df.head(5)