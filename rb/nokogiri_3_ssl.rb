# encoding : utf-8

require 'net/https'
require 'nokogiri'

url = 'https://www.google.co.jp/search?q=ruby+nokogiri&ie=utf-8&oe=utf-8'
url = URI.parse( url )

puts "URL=#{url}"
puts "Host:Port=#{url.host}:#{url.port}"


http = Net::HTTP.new( url.host, url.port )
http.use_ssl = true if url.port == 443
http.verify_mode = OpenSSL::SSL::VERIFY_NONE if url.port == 443
path = url.path
path += "?" + url.query unless url.query.nil?

p path

res = http.get( path )

p res

case res
  when Net::HTTPSuccess, Net::HTTPRedirection

    doc = Nokogiri::HTML(res.body)
    
    #puts doc
    puts doc.class 
     
	doc.xpath('//h3').each do |node|
	  puts node.text
	  puts node.css('a').attribute('href').value
	end

  else
    return "failed. " + res.to_s
end
