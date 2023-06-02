# Import packages
import os
import pandas as pd
from fuzzywuzzy import fuzz
# Change directory
# os.chdir(r"Your file path")# Import the customers data
filename = "customers lists input.xlsx"
customers = pd.read_excel(filename)  # Clean customers lists
A_cleaned = [customer for customer in customers["list_A"]
             if not (pd.isnull(customer))]
B_cleaned = [customer for customer in customers["list_B"].unique() if
             not (pd.isnull(customer))]
# Perform fuzzy string matching
tuples_list = [max([(fuzz.token_set_ratio(i, j), j)
                   for j in B_cleaned]) for i in A_cleaned]
# Unpack list of tuples into two lists
similarity_score, fuzzy_match = map(
    list, zip(*tuples_list))  # Create pandas DataFrame
df = pd.DataFrame({"list_A": A_cleaned, "fuzzy match": fuzzy_match,
                  "similarity score": similarity_score})
# Export to Excel
df.to_excel("Fuzzy String Matching.xlsx",
            sheet_name="Fuzzy String Matching", index=False)
