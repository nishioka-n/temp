import os
import sys
import openpyxl as px
from glob import glob



# 
SHEETS_NAMES = ['Display+Pop up']




def get_worksheet_cell_values(ws):
    lines = []
    for rowNo in range(2708, 2800):
        value1 = ws['F' + str(rowNo)].value
        value2 = ws['G' + str(rowNo)].value
        value3 = ws['I' + str(rowNo)].value
        if value1 != None:
            lines.append(f"'{value1}-{value2}', '{value3}'")
    return lines


def get_workbook_cell_values(xlsx_file_name):
    wb = px.load_workbook(xlsx_file_name, data_only=True)
    sheet_names = wb.get_sheet_names()
    print(sheet_names)

    lines = []
    for sheet_name in sheet_names:
        if not sheet_name in SHEETS_NAMES:
            continue

        ws = wb[sheet_name]
        lines.append("Sheet=" + ws.title)
        lines.extend(get_worksheet_cell_values(ws))
    return lines


def write_to_text_file(txt_file_name, lines):
    with open(txt_file_name, "w", encoding="UTF-8") as f:
        for line in lines:
            f.write(line + '\n')


def main(args):
    xlsx_file_name = 'サンプル.xlsx'
    lines = get_workbook_cell_values(xlsx_file_name)
    for line in lines:
        print(line)

if __name__ == '__main__':
    args = sys.argv[1:]
    main(args)
