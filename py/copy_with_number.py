# テスト用ダミーファイル作成
# ファイルを連番で命名してコピーする

import shutil
import os

# コピー元ファイル（このファイルの末尾に連番が付加されてコピーされる）
BASE_FILE = "empty.txt"

# 連番の開始
START_NUM = 1

# 連番の終了
END_NUM = 10

# 数値部分の桁数（ゼロ埋め）
NUM_LENGTH = 0  # 最大値の桁数より小さければ、最大値の桁数になる


# 数値部分のフォーマット文字列
def get_num_format() -> str:
    max_len = len(str(END_NUM)) 
    return '0' + str(max_len if max_len > NUM_LENGTH else NUM_LENGTH)


def main():
    if not os.path.isfile(BASE_FILE):
        print("File not found.")
        return

    filename, ext = os.path.splitext(BASE_FILE)
    num_fmt = get_num_format()
    for i in range(START_NUM, END_NUM + 1):
        num_part = format(i, num_fmt)
        copy_file_name = f"{filename}_{num_part}{ext}"
        print(copy_file_name)
        shutil.copy2(BASE_FILE, copy_file_name)


if __name__ == '__main__':
    main()
