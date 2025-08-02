import openpyxl
import tkinter as tk
from tkinter import filedialog
import pandas as pd
print('\033[2J')
print('\033[H')
# 9 - create a function that make deduction declaration automatically
# 10 - create a function that make encaissement declaration automatically
# 11 - create a new file just for the format conversion of the files without delete the old version
# 12 - show button to the user and ask him to download the file i want or interrested by

# 1- file uploade
# 2- check if the file is an excel file with .xlsx
# start the cleanning:
# 3- there is only one sheet in the file, if it is many ask to delete unimportant sheet and re-upload the file


def file_upload():
    while True:
        window = tk.Tk()
        window.withdraw()
        file_path = filedialog.askopenfilename(
            title='Select a file with .XLSX extension', filetypes=[('Excel files', '*.xlsx')])

        if file_path:
            try:
                uploaded_file = openpyxl.load_workbook(file_path)
                if len(uploaded_file.sheetnames) != 1:
                    print('Select a file with only one sheet, Delete unimportant sheet')
                    continue
                else:
                    print('File uploaded succesfully!!')
                    return file_path

            except:
                print('File not supported, import an Excel file')
        else:
            exit()


# file_upload()

# 4- clean column character, capitalize column name and use df.str.contains() to match with the required columns to avoid error from wrong spelling


def columns_formatting():
    uploaded_file = file_upload()

    df = pd.read_excel(uploaded_file)

    df.columns = (
        df.columns
        .str.capitalize()
        .str.strip()
        .str.replace(' ', '_')
    )
# # df.dropna()	Rows with any missing value
# df.dropna(axis=1)	Columns with any missing value
# df.dropna(how='all')	Rows where all values are NaN
    df = df.dropna(how='all')
    df = df.dropna(axis=1, how='all')
    df = df.drop(columns=[col for col in df.columns if (col is None) or (
        str(col).strip() == '') or (str(col).startswith('Unnamed'))])
# 5 - check if all the important columns is presents in the sheet - if not print columns name missing
# IMPORTANT COLUMNS CHECK
    df = df[['Date_facture', 'N°_de_facture', 'Mode_de_payement',
             'Fournisseur', 'Type', 'Credit', 'Debit', 'Taux', 'Tva']]

    df = df.dropna(subset=['Tva'])
    df = df[df['Tva'] != 0]
    df = df.dropna(subset=['N°_de_facture'])

# 5 - check if all the important columns is presents in the sheet - if not print columns name missing
# 6 - select only column required from the sheet and delete the others
    df[['Credit', 'Debit', 'Taux', 'Tva']] = df[['Credit', 'Debit',
                                                 'Taux', 'Tva']].apply(pd.to_numeric, errors='coerce')
    df['Date_facture'] = pd.to_datetime(
        df['Date_facture'], errors='coerce', utc=False).dt.date
    df[['N°_de_facture', 'Mode_de_payement', 'Fournisseur', 'Type']] = df[[
        'N°_de_facture', 'Mode_de_payement', 'Fournisseur', 'Type']].astype(str)

    # Column Mode de paiement formatting
    # VRT RECU//
    # VRT EMIS//
    # ENCAISSEMENT//
    # CHQ 0000370//
    # VIREMENT//
    # CHEQUE//
    # CARTE
    # VIT RECU//
    # VRT RCU//
    # ENVAISSEMENT//
    df.loc[df['Mode_de_payement'].str.contains(
        'vrt|vit|vir', case=False, na=False), 'Mode_de_payement'] = 4
    df.loc[df['Mode_de_payement'].str.contains(
        'caiss|espec|envais|encais', case=False, na=False), 'Mode_de_payement'] = 1
    df.loc[df['Mode_de_payement'].str.contains(
        'cheque|chq', case=False, na=False), 'Mode_de_payement'] = 2
    df.loc[df['Mode_de_payement'].str.contains(
        'prelev|prel', case=False, na=False), 'Mode_de_payement'] = 3
    df.loc[df['Mode_de_payement'].str.contains(
        'effet|eff', case=False, na=False), 'Mode_de_payement'] = 5
    df.loc[df['Mode_de_payement'].str.contains(
        'compensation|compens|compe', case=False, na=False), 'Mode_de_payement'] = 6
    df.loc[df['Mode_de_payement'].str.contains(
        'car', case=False, na=False), 'Mode_de_payement'] = 7
    # check if all mode of paiement got assignment
    for row in range(len(df)):
        row_value = df.iloc[row, 2]
        if not str(row_value).isdigit():
            print(
                f'\n Column name: |mode de paiement| not found in our database, change Value:|{row_value}| in the file')

    ###################
    # Create column ICE of companies
    entreprises_ice_if = [
        {"nom": "AHL DESIGN & ENGINEERING MAROC",
            "if": "14408306", "ice": "000031725000032"},
        {"nom": "BATIPLUS", "if": "66108192", "ice": "003581724000027"},
        {"nom": "BP", "if": "1084612", "ice": "001534931000016"},
        {"nom": "CARBO 3S", "if": "37699204", "ice": "002310691000094"},
        {"nom": "CELAYA AMENEGEMENTS", "if": "20787184", "ice": "001928134000088"},
        {"nom": "CFG BANK", "if": "1031055", "ice": "000084581000081"},
        {"nom": "EMIX ENGINEERING", "if": "31847634", "ice": "002169125000091"},
        {"nom": "GREEN WORK CONSULTING", "if": "66144603", "ice": "003611957000088"},
        {"nom": "ILEF", "if": "3300718", "ice": "001524978000057"},
        {"nom": "LUSELEC", "if": "15282601", "ice": "000250720000093"},
        {"nom": "LUSEO MEA", "if": "2222", "ice": "2222"},
        {"nom": "MAGHREB RESTAURATION CONSEIL",
            "if": "3382673", "ice": "001764430000097"},
        {"nom": "MARJANE", "if": "1085086", "ice": "001531173000020"},
        {"nom": "MAROC TELCOM", "if": "3332162", "ice": "001522585000066"},
        {"nom": "MB 2 WORKS", "if": "50259124", "ice": "002785583000052"},
        {"nom": "MLS MECHANICAL", "if": "3379547", "ice": "001534192000084"},
        {"nom": "ORANGE", "if": "1086826", "ice": "001524628000001"},
        {"nom": "PM OUTSOURCING", "if": "3379617", "ice": "001536493000037"},
        {"nom": "REDAL ELECTRICITE", "if": "3315990", "ice": "001562062000023"},
        {"nom": "REDAL EAU", "if": "", "ice": ""},
        {"nom": "RETIS INGENIERIE", "if": "65984292", "ice": "003431681000080"},
    ]

    df['ICE_FRS'] = ''
    df['IF'] = ''

    for row in range(len(df)):
        for entreprise in entreprises_ice_if:
            if df.iloc[row, 3].lower().strip() == entreprise['nom'].lower().strip():
                df.iloc[row, 9] = entreprise['ice']
                df.iloc[row, 10] = entreprise['if']

    df.to_excel('transformed_file.xlsx', index=False)


def separate_file():
    df = pd.read_excel('transformed_file.xlsx')
    #########
    df[['Credit', 'Debit', 'Taux', 'Tva']] = df[['Credit', 'Debit',
                                                 'Taux', 'Tva']].apply(pd.to_numeric, errors='coerce')
    df['Date_facture'] = pd.to_datetime(
        df['Date_facture'], errors='coerce', utc=False).dt.date
    df[['N°_de_facture', 'Mode_de_payement', 'Fournisseur', 'Type']] = df[[
        'N°_de_facture', 'Mode_de_payement', 'Fournisseur', 'Type']].astype(str)
    ##########

    credit_df = df[df['Credit'].notna() & (df['Credit'] != '')]
    credit_df.drop(['Debit'], axis=1, inplace=True)

    Debit_df = df[df['Debit'].notna() & (df['Debit'] != '')]
    Debit_df.drop(['Credit'], axis=1, inplace=True)

    credit_df.to_excel('credit_df.xlsx', engine='openpyxl', index=False)
    Debit_df.to_excel('Debit_df.xlsx', engine='openpyxl', index=False)

# 7 - separate deduction and encaissement TVA in two different excel files
# 8 - separate by month each file by month


def calculate_credit_declaration():
    credit_df = pd.read_excel('credit_df.xlsx')
    credit_df['Period'] = credit_df['Date_facture'].dt.strftime('%Y-%m')
    activate_function = input('Do you want to calculate credit tax(y/n):')
    if activate_function.isalpha and activate_function.lower()[0] == 'y':
        while True:
            year = input(
                'Enter the Year you are interrested by(exemple: 2019): ')
            if year.isdigit and len(str(year)) == 4:
                print('valid character!')
                break
            else:
                print('Invalid year, type again\n')

        while True:
            month = input('Enter the month you are interrested by(1 - 12): ')
            if month.isdigit and 1 <= int(month) <= 12:
                print('Valid input!')
                break
            else:
                print('Invalid input, type again\n')

        period = str(year)+'-'+str(month)
        filename = f'Credit_{year}_{month}'
        file = credit_df[credit_df['Period'] == period]
        file.to_excel(f'{filename}.xlsx', engine='openpyxl', index=False)
    else:
        return


def calculate_debit_declaration():
    debit_df = pd.read_excel('Debit_df.xlsx')
    debit_df['Period'] = debit_df['Date_facture'].dt.strftime('%Y-%m')
    activate_function = input('Do you want to calculate debit tax(y/n):')
    if activate_function.isalpha and activate_function.lower()[0] == 'y':
        while True:
            year = input(
                'Enter the Year you are interrested by(exemple: 2019): ')
            if year.isdigit and len(str(year)) == 4:
                print('valid character!')
                break
            else:
                print('Invalid year, type again\n')

        while True:
            month = input('Enter the month you are interrested by(1 - 12): ')
            if month.isdigit and 1 <= int(month) <= 12:
                print('Valid input!')
                break
            else:
                print('Invalid input, type again\n')

        period = str(year)+'-'+str(month)
        filename = f'Debit_{year}_{month}'
        file = debit_df[debit_df['Period'] == period]
        file.to_excel(f'{filename}.xlsx', engine='openpyxl', index=False)
    else:
        return


columns_formatting()
separate_file()
calculate_credit_declaration()
calculate_debit_declaration()


# wb = openpyxl.load_workbook('transformed_file.xlsx')
# ws = wb.active

# for row in range(1, 10):
#     for col in range(1, 15):
#         data = ws.cell(row=row, column=col).value
#         if data is None:
#             data = ''
#         print(f'{str(data):<35}', end=' | ')
#     print()
