import pandas as pd

df_msol = pd.read_csv("MSOLusersReport.csv")
df_eur = pd.read_csv("EURReport.csv")
print(df_msol.head(5))
print(df_eur.head(5))

df_merged = pd.merge(df_eur, df_msol, how="left", on="RelativePath_u")

filtered_df = df_merged[(df_merged['BlockCredential'].isnull())|(df_merged['BlockCredential'] == True)]
filtered_df = filtered_df[(filtered_df['SharingCapability'] != "Disabled")]
filtered_df = filtered_df[(filtered_df['LockState'] == "Unlock")]
filtered_df_head = filtered_df.head(2)
filtered_df_dict = filtered_df_head .to_dict()

print(filtered_df_dict)
