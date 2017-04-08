import groovy.json.*;

// ---------------------- 設定 ここから ---------------------
// ログファイル配置のルートディレクトリ
def ROOT_DIR = "logs"

// ファイルを絞り込む正規表現
def FILE_FILTER = /.*\.log/

// ログファイル名を出力する
def OUTPUT_LOGFILE_NAME = true

// ログの日時をローカルタイムに変換する
def CONV_LOCAL_TIME = true

// ログの日時フォーマット（ローカルタイムに変換する場合のみ使用）
def LOG_DATE_FORMAT = "yyyy-MM-dd'T'HH:mm:ssX"

// 出力する際の日時フォーマット（ローカルタイムに変換する場合のみ使用）
def OUTPUT_DATE_FORMAT = "yyyy/MM/dd HH:mm:ss" 

// 出力する際の各項目の区切り文字
def OUTPUT_DELIM = "\t"

// 抽出するログレベル（要素があれば処理）
def FILTER_LEVEL = [] // ["ERROR", "WARN"]

// 行番号を出力する
def OUTPUT_ROW_NUMBER = true

// ※ 出力する項目の選択と並び替えは、スクリプト内を編集してください。

// ---------------------- 設定 ここまで ---------------------

def fopen(path = ".") { new File(path); }

def getFiles(dir, filter) { dir.listFiles().findAll{ filter ? it.name ==~ filter : true }.sort{ it.lastModified() }}

def slurper = new JsonSlurper()

def processFiles = { dir ->

	getFiles(dir, FILE_FILTER).each { file ->
		if (OUTPUT_LOGFILE_NAME) println "\nLog File:\t${file.path}"
		
		file.eachLine("UTF-8", { line, rowNum  ->
			def map = [:]
			try {
				map = slurper.parseText(line)
			} catch (JsonException ex) {
				println line 
				return
			}
			
			if (FILTER_LEVEL && !FILTER_LEVEL.contains(map.level)) return
			
			datetime = map.time
			if (CONV_LOCAL_TIME) {
				datetime = Date.parse(LOG_DATE_FORMAT, datetime).format(OUTPUT_DATE_FORMAT, TimeZone.getDefault())
			}
			
			// 出力する項目
			output_fields = [datetime, map.level, map.message, map.exception?:""]
			
			if (OUTPUT_ROW_NUMBER) {
				output_fields.add(0, String.format("%06d", rowNum));
			}
			
			println output_fields.join(OUTPUT_DELIM)
		})
	} 
}

def rootDir = ROOT_DIR ? fopen(ROOT_DIR) : fopen()
processFiles(rootDir)
rootDir.eachDirRecurse() { processFiles(it) } 

