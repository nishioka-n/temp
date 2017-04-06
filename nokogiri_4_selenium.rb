# encoding : utf-8

#!/usr/bin/ruby
require "nokogiri"
require "selenium-webdriver"

driver = Selenium::WebDriver.for :firefox
driver.manage.timeouts.implicit_wait = 10 # seconds

driver.get "http://www.yahoo.co.jp"
doc = Nokogiri::HTML driver.page_source.encode("UTF-8") 

p doc.title
driver.quit
