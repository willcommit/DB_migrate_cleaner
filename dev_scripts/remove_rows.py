import pandas as pd
import helpers

excel_new_data = helpers.open_filedialog('DYNAMICS IMPORT')
excel_delete_ref = helpers.open_filedialog('DELETE')

df_new = pd.read_excel(excel_new_data, header=2)
df_delete = pd.read_excel(excel_delete_ref)

matching_cols = set(df_new['Artikelnr']).intersection(set(df_delete['Nr']))
print(len(matching_cols))


cols_dropped = []
count = 0

for index, data in df_new.iterrows():
        for nr in matching_cols:
            if (data.Artikelnr == nr):
                df_new.drop([index], inplace=True)
                cols_dropped.append(data.Artikelnr)
                count += 1

non_matching_cols1 = set(df_delete['Nr']).difference(set(cols_dropped))
print(len(non_matching_cols1))

non_matching_cols2 = set(cols_dropped).difference(set(df_delete['Nr']))
print(len(non_matching_cols2))

helpers.save_to_csv(non_matching_cols2, "./non_matching_cols2.csv")
helpers.save_to_csv(non_matching_cols1, "./non_matching_cols1.csv")

print("{} {} rows deleted and {} remaing".format(count,len(cols_dropped),len(df_new.index)))

df_new.to_excel("test.xlsx", index=False)