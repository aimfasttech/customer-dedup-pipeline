# ============================================
# Export & Reporting Module
# Author: Stephen Abiodun | AimFastTech
# ============================================

import pandas as pd
import numpy as np

# ---- EXECUTIVE SUMMARY ----
summary_data = {
    'Metric': [
        'Total Records Processed',
        'Exact Duplicates Removed',
        'Fuzzy Matches Flagged',
        'Final Clean Records'
    ],
    'Value': [
        len(df_original),
        len(df_removed),
        len(df_fuzzy_flagged),
        len(df_clean)
    ],
    'Manager Note': [
        'Initial raw dataset size',
        '100% safe automated removals',
        'Requires human eye to confirm',
        'Ready for production use'
    ]
}

df_summary = pd.DataFrame(summary_data)

# ---- OPEN THE GATE ----
with pd.ExcelWriter('Customer_Data_Audit.xlsx') as gate_keeper:

    # Post Summary first
    df_summary.to_excel(gate_keeper,
                sheet_name='Executive_Summary', index=False)

    # Post Golden Records
    df_clean.to_excel(gate_keeper,
                sheet_name='Final_Golden_Records', index=False)

    # Post Flagged Records
    df_fuzzy_flagged.to_excel(gate_keeper,
                sheet_name='Flagged_For_Review', index=False)

    # Post Audit Trail
    df_removed.to_excel(gate_keeper,
                sheet_name='Audit_Trail_Removed', index=False)

# The gate locks itself. Mission complete.
print("✅ Excel Report Generated!")
print(df_summary)
