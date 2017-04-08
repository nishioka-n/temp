#!/usr/bin/env ruby
# coding:utf-8

filename = "SourceFile.txt";
delim = "//";
max_len = 0
src_lines = []
cmt_lines = []

File.open(filename, "r:UTF-8") do |f|
	f.each_line do |line|
		sep_line = line.split(delim)
		src = sep_line[0].nil? ? "" : sep_line[0].chomp
		cmt = sep_line[1].nil? ? "" : sep_line[1].chomp
		max_len = [max_len, src.length].max
		src_lines.push src
		cmt_lines.push cmt
	end
end

out_lines = src_lines.zip(cmt_lines)
out_lines.each do |line|
	puts line[0].ljust(max_len) + delim + " " + line[1]
end

