import pandas as pd
import helpers

excel_old_data = helpers.open_filedialog('NAV EXPORT')
excel_new_data = helpers.open_filedialog('DYNAMICS IMPORT')
excel_delete_ref = helpers.open_filedialog('DELETE')

df_old = pd.read_excel(excel_old_data)
df_new = pd.read_excel(excel_new_data)
df_delete = pd.read_excel(excel_delete_ref)

#Deleting rows according to file
df_old = helpers.delete_rows(df_delete, df_old)

#Finding cols that match and don't
matching_cols = set(df_old.columns).intersection(set(df_new.columns))
non_matching_cols = set(df_new.columns).difference(set(df_old.columns))

#Combining files to final import file
df_final = df_new.append(df_old[matching_cols], sort=False, ignore_index=True)

#TODO Cleaning data - move to helpers, create config file
df_final = df_final.replace('Nej', False, regex=True)
df_final['Hemsida'] = df_final['Hemsida'].apply(helpers.find_clean_website)

#Save to files
save_location = helpers.save_filedialog()
df_final.to_excel(save_location, index=False)
helpers.save_to_csv(non_matching_cols, "./non_matching_cols.csv")

print("Complete! {} non matching cols".format(len(non_matching_cols)))
