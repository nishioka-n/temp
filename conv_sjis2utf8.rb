# coding:utf-8

=begin 
 文字コード変換 (SJIS - > UTF-8)
=end 

if ARGV.empty?
	puts "Please specify file name."
	exit
end

lines = []
fileName = ARGV[0]

File.open(fileName, "r:CP932:UTF-8") do |f|
	lines = f.readlines
end

baseName = File.basename(fileName, ".*")
extention = File.extname(fileName)
newName = baseName + "_utf8" + extention

File.open(newName, "w+b") do |f|  # バイナリモードで開かないと、改行コードが勝手に変換されてしまう
	lines.each do |line|
		f.print line.chomp + "\n"
	end
end

puts %Q{"#{newName}" created.}

