import os
import sys
import openpyxl as px
from glob import glob
from openpyxl.utils.cell import coordinate_from_string, column_index_from_string, get_column_letter

# xy = coordinate_from_string('A4') # returns ('A',4)
# col = column_index_from_string(xy[0]) # returns 1
# row = xy[1]

# ファイル名
XLSX_FILE_NAME = ''

# 言語数
LANGUAGE_COUNT = 20

# 対象シート名
SHEETS_NAMES = ['Display+Pop up']


def escape4sql(value):
    return value.replace('"', '\"')

# 
def get_worksheet_cell_values(ws):
    lines = []

    # 英語の列
    first_col = 'I'  # 設定から
    first_col_index = column_index_from_string(first_col)

    first_row = 16  # 設定から
    language_row = 14  # 設定から

    for row_index in range(first_row, first_row + 30):
        item_type = ws['F' + str(row_index)].value
        item_id = ws['G' + str(row_index)].value
        if item_type == None:
            continue

        # メッセージ言語数分処理
        for col_index in range(first_col_index, first_col_index + LANGUAGE_COUNT):
            # print(f'col_index={col_index}')
            lang_code = ws.cell(column=col_index, row=language_row).value  # 毎回取得は効率悪いので改善
            cell = ws.cell(column=col_index, row=row_index)
            cell_addr = cell.coordinate
            message = cell.value
            if not message:
                continue

            # エスケープ処理


            # lines.append(f"'{item_type}-{item_id}', '{message}'")
            print(f"'{cell_addr}:  {item_type}-{item_id}', '{lang_code}', '{message}'")

    return lines


def get_workbook_cell_values(xlsx_file_name):
    wb = px.load_workbook(xlsx_file_name, data_only=True, read_only=True)
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
    xlsx_file_name = XLSX_FILE_NAME
    lines = get_workbook_cell_values(xlsx_file_name)
    for line in lines:
        print(line)

if __name__ == '__main__':
    args = sys.argv[1:]
    main(args)
