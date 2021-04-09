
from datetime import datetime
from glob import glob
import os
import shutil

# ===== 設定 ===== #
# コピー先ディレクトリ
TARGET_DIR = r'../UPDATED'
# 検索対象
SEARCH_PATH = "**/*.*"
# 除外する拡張子
EXCLUDE_EXTS = [".dll", ".log", ".cache"]
# 対象とするファイルの更新日時
START_DATE = "2019/01/28 14:00"
# 対象とするファイルの更新日時のフォーマット
START_DATE_FORMAT = '%Y/%m/%d %H:%M'


def main():

    dt = datetime.strptime(START_DATE, START_DATE_FORMAT)

    for file_path in glob(SEARCH_PATH, recursive=True):
        _, ext = os.path.splitext(file_path)
        if ext in EXCLUDE_EXTS:
            continue

        ts = os.path.getmtime(file_path)
        mt = datetime.fromtimestamp(ts)
        if mt >= dt:
            dir_path, file_name = os.path.split(file_path)
            target_dir_path = os.path.join(TARGET_DIR, dir_path)
            print(mt, target_dir_path, file_name)
            if not os.path.exists(target_dir_path):
                print("ディレクトリ作成:", target_dir_path)
                os.makedirs(target_dir_path)
            shutil.copy2(file_path, target_dir_path)

if __name__ == '__main__':
    main()
