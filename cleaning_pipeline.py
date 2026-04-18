# ============================================
# Customer Deduplication Pipeline
# Author: Stephen Abiodun | AimFastTech
# ============================================

import pandas as pd
import numpy as np
from rapidfuzz import process, fuzz

# ---- SAMPLE DATA ----
data = {
    "client_id": [1, 2, 3, 4, 5],
    "Name": ["John Smith", "JOHN SMITH", "Mary Grace",
             "jon smith", "Grace Mary"],
    "Email": ["john@email.com", "john@email.com",
              "mary@email.com", "john@email.com",
              "grace@email.com"],
    "timestamp": ["2024-01-01", "2024-03-01",
                  "2024-02-01", "2024-04-01",
                  "2024-01-15"]
}

df = pd.DataFrame(data)

# ---- STEP 1: NORMALIZE ----
df['name_clean'] = df['Name'].str.lower().str.strip()

# ---- STEP 2: SORT ----
df_sorted = df.sort_values('timestamp', ascending=False)

# ---- STEP 3: REMOVE EXACT DUPLICATES ----
df_clean = df_sorted.drop_duplicates(
    subset='client_id',
    keep='first'
)

# ---- STEP 4: FUZZY MATCHING ----
names = df_clean['name_clean'].tolist()
target_name = "smith john"

potential_matches = process.extract(
    target_name,
    names,
    scorer=fuzz.token_sort_ratio,
    score_cutoff=85
)

print("✅ Clean Data:")
print(df_clean)
print("\n🔍 Fuzzy Matches Found:")
print(potential_matches)
