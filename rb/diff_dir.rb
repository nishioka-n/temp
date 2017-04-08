# encoding : utf-8

if ARGV.length < 2
	puts "Usage: #{$0} dir0 dir1"
	exit
end

dir0 = ARGV[0]
dir1 = ARGV[1]

files0 = Dir.chdir(dir0) { Dir.glob("**/*") }
files1 = Dir.chdir(dir1) { Dir.glob("**/*") }

p files0
p files1

puts "#{dir0} にあって #{dir1} にないファイル：#{files0 - files1}"
(files0 - files1).each do |f|
	puts f
end

puts "#{dir1} にあって #{dir0} にないファイル：#{files1 - files0}"
(files1 - files0).each do |f|
	puts f
end

