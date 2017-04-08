# encoding : utf-8

require 'nokogiri'

html = %q{
<div class="entry-content">
   <p>Some text...</p>
</div>

         <p>
            <a>abc</a>
            <a>pqr></a>
         </p>
         <table>
           <tr>
             <td><p>example</p></td>
             <td><p>find</p></td>
             <td><p>by</p></td>
             <td><p>ID</p></td>
           </tr>
         </table>
        <p><p>zzzz</p>nnnnn</p>
        <u>sfds<u>
        
}

str =<<__HERE__
<div class="entry-content">
   <p>Some text...</p>
</div>
__HERE__

    doc = Nokogiri::HTML(html)
    
    #puts doc
    puts doc.class 
    puts "doc.root.name = #{doc.root.name}"
    
	puts "tr.parent = #{doc.xpath('//tr').first.parent.name}"

	doc.xpath('//td/p').each do |node|
	  puts "td/p = #{node.text}"
	  # puts node.css('a').attribute('href').value
	end


