@echo off
ruby -x "%~f0" %*
goto :EOF

#!ruby
#---------------ruby script starts here
puts "hello, rb.bat"
#---------------ruby script ends here
__END__
:EOF