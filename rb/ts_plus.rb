# encoding : utf-8

ONE_MINUTE = 60 # seconds

if ARGV.size == 0
	puts "Specify file."
	exit
end

file_name = ARGV[0]

minites = 1
if ARGV.size > 1
	minites = ARGV[1].to_i
end

now = Time.now
ut = now + (minites * ONE_MINUTE)

File::utime(ut, ut, file_name)

