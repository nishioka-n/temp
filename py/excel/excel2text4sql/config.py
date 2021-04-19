# 翻訳リストのExcelファイルからSQL(DML : DELETE, INSERT)を生成しファイル出力
# 設定ファイル
# 
# 生成する対象に応じて、「対象シート名」や「」
# 
# いずれは、JSONかYAMLなどに変更するつもりだが、簡単なソース方式で実装
# 

# セル内の改行(Lf) をエスケープするか（True: "\\n" ; False: 出力ファイルの実際の改行="\n"）
ESCAPE_LF = False

# DELETE文のフォーマット（既存の手動作成の書式を貼り付け）
DELETE_SQL_ITEM = "delete from item_master where item_type='{item_type}' and item_id='{item_id}';"

# DELETE文(言語単位)のフォーマット（既存の手動作成の書式を貼り付け）
DELETE_SQL_LANG = "delete from item_master where item_type='{item_type}' and item_id='{item_id}' and language_code='{language_code}';"

# INSERT文のフォーマット（既存の手動作成の書式を貼り付け）
INSERT_SQL = "insert into item_master values('{item_type}','{item_id}','{language_code}',E'{message}',now());"


# 共通設定
common_config = {
    # 入力ファイル名（デフォルト）： コマンドライン引数（第一引数）で指定された場合は上書き
    "input_file_name": "翻訳リスト.xlsx",
    # すべての言語コードの数
    "language_count": 20,
    # 対象シート名： ここに指定しなければ処理されない
    "sheet_names": ["Display+Pop up",  "Emailメッセージ"],
    # 出力ファイル名（デフォルト）： コマンドライン引数（第二引数）で指定された場合は上書き
    "output_file_name": "result.sql",
    # 出力ファイルの文字コード
    "output_encoding": "UTF-8",
	# 出力ファイルの改行コード
	"output_newline": "\n",
}


# シートごとの設定
sheet_config = {
    # シート名
    "Display+Pop up": {
        # 言語コードの行
        "language_code_row": 14,
        # 翻訳リストアイテムの開始行
        "item_start_row": 16,
        # item_type（キー項目）の列
        "item_type_col": "F",
        # item_id（キー項目）の列
        "item_id_col": "G",
        # language_code（キー項目）の最初の列（英語列）
        "language_code_1st_col": "I",
        # 対象を絞り込む条件列
        "target_cond_col": "A", 
        # 対象を絞り込む条件文字列（空文字なら何もしない）
        "target_cond_str": "",
        # 対象言語（空のリストなら、すべてが対象）
        "target_language_codes": ["en", "el"],
    },
    # シート名
    "Emailメッセージ": {
        # 言語コードの行
        "language_code_row": 5,
        # 翻訳リストアイテムの開始行
        "item_start_row": 7,
        # item_type（キー項目）の列
        "item_type_col": "F",
        # item_id（キー項目）の列
        "item_id_col": "G",
        # language_code（キー項目）の最初の列（英語列）
        "language_code_1st_col": "H",
        # 対象を絞り込む条件列
        "target_cond_col": "A", 
        # 対象を絞り込む条件文字列（空文字なら何もしない）
        "target_cond_str": "",
        # 対象言語（空のリストなら、すべてが対象）
        "target_language_codes": [],
    }
}


if __name__ == "__main__":
    print(common_config)
