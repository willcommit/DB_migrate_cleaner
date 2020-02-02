import pandas as pd
import helpers

excel_pricelist = 'C:/Users/welfv/OneDrive - Furuno Danmark A S/MigrationNav/Tabell 27 Artiklar/items_fran_nav.xlsx'
excel_delete_ref = 'C:/Users/welfv/OneDrive - Furuno Danmark A S/MigrationNav/Tabell 27 Artiklar/items_remove.xlsx'

df_pricelist= pd.read_excel(excel_pricelist)
df_delete = pd.read_excel(excel_delete_ref)

print(df_delete[df_delete.duplicated(keep=False)])

# articles_to_check = df_delete['Nr']
# locked_articles= []
# count = 0

# for index, data in df_pricelist.iterrows():
#     if (data.Spärrad == 'Ja'):
#         locked_articles.append(data.Nr)

# print(len(locked_articles))

# non_matching_cols = set(locked_articles).difference(set(articles_to_check))
# print(len(non_matching_cols))

# helpers.save_to_csv(non_matching_cols, "./spärrade.csv")

