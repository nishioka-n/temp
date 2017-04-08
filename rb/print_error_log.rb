#!/usr/bin/env ruby
# coding:utf-8

# デフォルトファイル名（コマンドライン引数で上書き）
filenames = %w{ error.log }

# ログレベルの前に出力される定型文字列数
num = "YYYY-MM-DD HH:MM:SS,NNN".length

if ARGV.length > 0
	filenames = ARGV
end

filenames.each do |filename|
	outputflg = false
	puts filename
	File.open(filename, "r:UTF-8") do |f|
		f.each_line do |line|
			if line =~ /^.{#{num}}\sERROR\s/
				outputflg = true
			elsif line =~ /^.{#{num}}\s(TRACE|DEBUG|INFO|WARN)\s/
				outputflg = false;
			end
			puts "%6d\t"%($.) + line if outputflg	# ログに"100%;"などの文字列が含まれるとエラーとなるためフォーマット文字列と分離
		end
	end
end
