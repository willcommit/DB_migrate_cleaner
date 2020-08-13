#SERVICE ITEMS

import pandas as pd
import helpers

excel_old_data = helpers.open_filedialog('NAV EXPORT')
excel_new_data = helpers.open_filedialog('DYNAMICS IMPORT')
excel_delete_ref = helpers.open_filedialog('DELETE')

df_old = pd.read_excel(excel_old_data)
df_new = pd.read_excel(excel_new_data)
df_delete = pd.read_excel(excel_delete_ref)

#Deleting rows according to file
df_old = helpers.delete_rows(df_delete, df_old, 'Nr')

#Cleaning/Changing name on columns, fit import
df_old = helpers.change_item_col(df_old)

#Finding cols that match and don't
matching_cols = set(df_old.columns).intersection(set(df_new.columns))
non_matching_cols = set(df_old.columns).difference(set(df_new.columns))

helpers.save_to_csv(non_matching_cols, "./non_matching_cols.csv")
helpers.save_to_csv(matching_cols, "./matching_cols.csv")

#Combining files to final import file
df_final = df_new.append(df_old[matching_cols], sort=False, ignore_index=True)

#Cleaning data - move to helpers. create config file for changes?
df_final = helpers.data_cleaner(df_final, "Ja")
df_final = helpers.data_cleaner(df_final, "Nej")
df_final = helpers.data_cleaner(df_final, "TB=pris-kostnad")

#Save to files
save_location = helpers.save_filedialog()
df_final.to_excel(save_location, index=False)

print("Complete! {} non matching cols".format(len(non_matching_cols)))
