import re
import pandas as pd
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

rows_to_delete = []

def open_filedialog(file_type):
    root = tk.Tk()
    root.filename = askopenfilename(initialdir = "./",title = "Select {} file".format(file_type), filetypes = (("Excel","*.xlsx"),("all files","*.*")))
    filename = root.filename
    print (root.filename)
    root.destroy()

    return str(filename)

def save_filedialog():
    root = tk.Tk()
    root.filename =  asksaveasfilename(initialdir = "./",title = "Save to",filetypes = (("Excel","*.xlsx"),("all files","*.*")))
    filename = root.filename
    print (root.filename)
    root.destroy()

    return str(filename)


def find_clean_website(website):
    if re.search('\www.*', str(website)):
        return website
    else:
        return ''

def find_delete_rows(df):

    rows_to_delete.clear

    for row, data in df.iterrows():
        if data.Delete == 'Ja':
            rows_to_delete.append(data.Nr)
    
    

def delete_rows(df_delete, df_main):

    find_delete_rows(df_delete)

    print("{} rows will be deleted".format(len(rows_to_delete)))

    count = 0

    for index, data in df_main.iterrows():
        for nr in rows_to_delete:
            if (data.Nr == nr):
                df_main.drop([index], inplace=True)
                count += 1
    
    print("{} rows deleted and {} remaing".format(count, len(df_main.index)))

    return df_main

def save_to_csv(set, filename):
    csv_file = open(filename, 'w')

    for item in set:
        csv_file.write("{} \n".format(item))

    csv_file.close()

# if __name__ == "__main__":
