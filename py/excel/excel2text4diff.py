import os
import sys
import openpyxl as px
from glob import glob

# Row separator
ROW_SEP = "-" * 100

# True: Output column name. False : Output cell address.
ONLY_COLUMN = True

# Worksheet exclusion list.
SHEETS_EXCLUDED = ["temp"]

# Column exclusion list.
COLUMNS_EXCLUDED = ["A", "B"]


def get_worksheet_cell_values(ws):
    lines = []
    for row in ws.rows:
        lines.append(ROW_SEP)
        for cell in row:
            if cell.column in COLUMNS_EXCLUDED:
                continue
            if cell.value is not None:
                addr = cell.column if ONLY_COLUMN else cell.coordinate
                lines.append("%s=%s" % (addr, cell.value))
    lines.append("")
    return lines


def get_workbook_cell_values(xlsx_file_name):
    wb = px.load_workbook(xlsx_file_name, data_only=True)
    sheet_names = wb.get_sheet_names()
    print(sheet_names)

    lines = []
    for sheet_name in sheet_names:
        if sheet_name in SHEETS_EXCLUDED:
            continue
        ws = wb.get_sheet_by_name(sheet_name)
        lines.append("Sheet=" + ws.title)
        lines.extend(get_worksheet_cell_values(ws))
    return lines


def write_to_text_file(txt_file_name, lines):
    with open(txt_file_name, "w", encoding="UTF-8") as f:
        for line in lines:
            f.write(line + '\n')


def main(args):
    # Process the files if specified, or glob files.
    file_names = args or glob('*.xlsx')
    for xlsx_file_name in file_names:
        print(xlsx_file_name)
        base_name, ext = os.path.splitext(xlsx_file_name)
        txt_file_name = base_name + ".txt"
        lines = get_workbook_cell_values(xlsx_file_name)

        try:
            write_to_text_file(txt_file_name, lines)
        except PermissionError as pe:
            print(pe)


if __name__ == '__main__':
    args = sys.argv[1:]
    main(args)
