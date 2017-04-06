<%@ page contentType="text/html; charset=utf-8"
          import="java.io.*,java.util.*" %>
<html>
<head>
<title>File List</title>
<style>
td {
	padding: 5px;
}
</style>
<body>
<table border="1" style="border-collapse: collapse;">
<tr>
   <th>File Name</th><th>Size</th><th>Last Modified</th>
</tr>
<%
	String dirPath = "./files";
	File dir = new File(application.getRealPath(dirPath));
	File[] files = dir.listFiles();
	for (int i = 0; i < files.length; i++) {
		File file = files[i];
		String fileName = file.getName();
%>
   <tr>
   <td><a href="<%= dirPath + fileName %>"><%= fileName %></a></td>
   <td align="right">
   <%
   if (file.isDirectory()){
       out.print("<br />");
   } else {
       out.print(Math.ceil(file.length()/1024+1) + " KB");
   }
   %>
   </td>
   <td><%= (new Date(file.lastModified())).toString() %></td>
   </tr>
 <% } %>
 </table> 

</body>
</html>
