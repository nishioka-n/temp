# encoding : utf-8

require 'nokogiri'

doc = Nokogiri::XML.parse(File.open('info.xml'))

details = doc.css('details').find{|node| node.css('id').text == "5678"}

email = details.css('email').text # => "zzzz@zzz.com"

images = details.css('image').map(&:text) # => ["images/4.jpg", "images/5.jpg"]