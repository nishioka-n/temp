
from datetime import datetime
import os
import sys
import shutil

# 対象ファイル名 （指定があれば、引数なしで実行するとコピー）
FILE_NAMES = []

# コピー後に読取専用にするか
IS_READONLY = True


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    if len(args) == 0 and FILE_NAMES:
        args.extend(FILE_NAMES)

    if (len(args) == 0):
        print('Usage: {} filename'.format(os.path.basename(sys.argv[0])))
        quit()

    # ファイルを複数ドラッグされた場合に対応し、引数の数分処理する
    for file_path in args:
        copy_with_timestamp(file_path)


def set_readonly(file_path):
    from stat import S_IRUSR
    os.chmod(file_path, S_IRUSR)


def get_file_mtime(file_path: str) -> str:
    ts = os.path.getmtime(file_path)
    mt = datetime.fromtimestamp(ts)
    return datetime.strftime(mt, '%Y%m%d%H%M%S')


def copy_with_timestamp(file_path: str):
    dir_name, file_name = os.path.split(file_path)
    base_name, ext = os.path.splitext(file_name)
    mt_str = get_file_mtime(file_path)
    new_file_name = "{}_{}{}".format(base_name, mt_str, ext)
    new_file_path = os.path.join(dir_name, new_file_name)
    shutil.copy2(file_path, new_file_path)
    if IS_READONLY:
        set_readonly(new_file_path)


if __name__ == '__main__':
    main()
