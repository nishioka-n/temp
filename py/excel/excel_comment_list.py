import os
import openpyxl as px
import glob

ROW_SEP = "-" * 100

# 出力するファイルの文字コード
OUT_FILE_ENCODING = 'utf-8'

# 各コメントごとのフォーマット
OUTPUT_FORMAT = '{address}\t"{comment}"'

# 対象シート名 （指定してあれば、こちらだけが対象）
INCL_WS_NAMES = ["5-1.要件_システム状態遷移"]

# 除外するシート名
EXCL_WS_NAMES = ["表紙Cover", "改訂履歴", "一覧"]


def get_worksheet_comment_values(ws):
    lines = []
    for row in ws.rows:
        # lines.append(ROW_SEP)
        for cell in row:
            if cell.comment is None:
                continue
            address = cell.coordinate
            comment = cell.comment.text
            item_dic = dict(address=address, comment=comment)
            out_str = OUTPUT_FORMAT.format(**item_dic)
            lines.append(out_str)
    return lines


def get_workbook_cell_values(xlsx_file_name):
    wb = px.load_workbook(xlsx_file_name)
    sheet_names = [sn for sn in wb.sheetnames if sn not in EXCL_WS_NAMES]

    lines = []
    for sheet_name in sheet_names:
        if INCL_WS_NAMES and sheet_name not in INCL_WS_NAMES:
            continue
        ws = wb[sheet_name]
        lines.append("Sheet=" + ws.title)
        lines.extend(get_worksheet_comment_values(ws))
    return lines


def write_to_text_file(txt_file_name, lines):
    with open(txt_file_name, "w") as f:
        for line in lines:
            f.write(line + '\r\n')


def main():

    file_names = glob.glob('*.xlsx')
    for xlsx_file_name in file_names:
        print(xlsx_file_name)
        base_name, ext = os.path.splitext(xlsx_file_name)
        txt_file_name = base_name + ".txt"
        lines = get_workbook_cell_values(xlsx_file_name)
        if lines:
            write_to_text_file(txt_file_name, lines)

if __name__ == '__main__':
    main()
