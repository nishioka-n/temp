#!/bin/bash

# ---------- 設定 ----------

# SQLを記述したファイル（コマンドライン引数で上書き）
SQL_FILE_NAME=default.sql

# HTML出力テンプレートファイル
TEMPLATE_FILE_NAME=template.html
# --------------------------

# 第一引数に指定があれば、実行するSQLファイルを切り替える
if [ ! -z "$1" ]; then
	SQL_FILE_NAME=$1
fi

if [ ! -e $SQL_FILE_NAME ]; then
	echo "Specified SQL File Not Found."
	exit 
fi

# SQL実行
sqlresult=`mysql -u root -pmysql --html test < $SQL_FILE_NAME`


# テンプレートファイル読込
template=`cat $TEMPLATE_FILE_NAME`

# ホスト名 埋め込み
output_result=${template//HOST_NAME/`hostname`}

# 実行時間 埋め込み
output_result=${output_result//EXECUTED_DATETIME/`date '+%Y/%m/%d %T'`}

# NULL の文字列消す  ＊ TODO 遅くて使えないので、sed に変更 ＊
# sqlresult=${sqlresult//>NULL</><}
sqlresult=`echo $sqlresult | sed -e 's/>NULL</></g'`

# SQL実行結果 埋め込み
output_result=${output_result//SQL_RESULT/$sqlresult}

# 実行SQL 埋め込み
executed_sql=`cat $SQL_FILE_NAME`
output_result=${output_result//EXECUTED_SQL/$executed_sql}


echo "$output_result"

