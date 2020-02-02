import pandas as pd
import helpers

excel_pricelist = 'C:/Users/welfv/OneDrive - Furuno Danmark A S/MigrationNav/Tabell 27 Artiklar/pricelist2.xlsx'
excel_delete_ref = 'C:/Users/welfv/OneDrive - Furuno Danmark A S/MigrationNav/Tabell 27 Artiklar/remove_input.xlsx'

df_pricelist= pd.read_excel(excel_pricelist)
df_delete = pd.read_excel(excel_delete_ref, header=2)

articles_to_delete = df_delete['Artikelnr']
articles_to_keep = df_pricelist['Artikel']

# print(articles_to_delete)
# print(articles_to_keep)

matching_cols = set(articles_to_keep).intersection(set(articles_to_delete))
print(len(matching_cols))

print(matching_cols)

count = 0

for index, data in df_delete.iterrows():
        for nr in matching_cols:
            if (data.Artikelnr == nr):
                df_delete.drop([index], inplace=True)
                count += 1

print("{} rows deleted and {} remaing".format(count, len(df_delete.index)))

df_delete.to_excel("test.xlsx", index=False)
              
#Hitta alla rader i df_delete och samla dessa nummer i en remove set
# 
#Importera Prislista till DF, samma alla artikel nummer i ett set

# Testa om det finns artikel nummer i båda listor som matchar
#Testa hur många som inte matchar också
