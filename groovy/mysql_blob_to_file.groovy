import groovy.sql.Sql

def JDBC_URL = "jdbc:mysql://localhost:3306/sakila?useUnicode=true&characterEncoding=UTF-8"
def USER = "root"
def PASS = "mysql"

Sql sql = Sql.newInstance(JDBC_URL, USER, PASS, "com.mysql.jdbc.Driver")
          
sql.eachRow("SELECT first_name, picture FROM sakila.staff") { row ->
	String name = row['first_name']
	byte[] blob = row['picture']
	if (blob != null) {
		def fos = new FileOutputStream("${name}.jpg")
		fos.write(blob, 0, blob.length)
		fos.close()
	} 
}

sql.connection.close()

