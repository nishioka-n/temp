import sys
import openpyxl as px
import re
from glob import glob

# 検索キーワード(正規表現)のリスト
SEARCH_REGEXPS = ["キーワード"]

# 検索するExcelファイル（コマンドライン引数優先）
# 両方とも渡されなければ、カレントディレクトリのすべてのExcelファイル（*.xlsx）
SEARCH_TARGET_FILES = []

# 結果を出力するファイル名（指定がない場合は、標準出力）
RESULT_FILE_NAME = "excel_search_result.txt"


def write_file(file_name: str, lines: list, nl: bool=True, encoding="UTF-8"):
    with open(file_name, "w", encoding=encoding) as f:
        if nl:
            for line in lines:
                f.write(line + "\n")
        else:
            f.writelines(lines)


def get_worksheet_cell_values(ws):
    lines = []
    for row in ws.rows:
        for cell in row:
            value = cell.value
            addr = cell.coordinate
            if value:
                for kw in SEARCH_REGEXPS:
                    if re.search(kw, str(value)):
                        lines.append("{}={}".format(addr, value))
    if not lines:
        lines.append("(Not Found)")

    lines.append("")
    return lines


def exec_search(file_name):
    wb = px.load_workbook(file_name)
    lines = []
    lines.append("File=" + file_name)
    for sheet_name in wb.get_sheet_names():
        ws = wb.get_sheet_by_name(sheet_name)
        lines.append("Sheet=" + ws.title)
        lines.extend(get_worksheet_cell_values(ws))

    return lines


def main(args=None):
    file_names = args or glob('*.xlsx')
    lines = []
    for xlsx_file_name in file_names:
        print("file={}".format(xlsx_file_name))
        lines.extend(exec_search(xlsx_file_name))

    if RESULT_FILE_NAME:
        write_file(RESULT_FILE_NAME, lines)
    else:
        for line in lines:
            print(line)


if __name__ == '__main__':
    args = sys.argv[1:] or SEARCH_TARGET_FILES
    main(args)
