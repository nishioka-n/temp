import groovy.sql.Sql

// Connection Settings
def DB_SCHEMA = "test"
def DB_USER = "root"
def DB_PASS = "mysql"

def conn = Sql.newInstance("jdbc:mysql://localhost:3306/${DB_SCHEMA}", DB_USER, DB_PASS, "org.gjt.mm.mysql.Driver")

// SQL Params
def TABLE_SCHEMA = DB_SCHEMA
def TABLE_NAME = "table1"

def SELECT_SQL = "select COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS where TABLE_SCHEMA = ? and TABLE_NAME = ? order by ORDINAL_POSITION"

def params = [TABLE_SCHEMA, TABLE_NAME]
def cols = []

conn.eachRow(SELECT_SQL, params) { row ->
	//cols.add(row.COLUMN_NAME)
	cols << row.COLUMN_NAME
}

def resultSql = "select " + cols.join(", ") + " from ${TABLE_NAME}"

println resultSql

/*

Named and named ordinal parameters
Several of the methods in this class (ones which have a String-based sql query and params in a List<Object> or Object[] or Map) support named or named ordinal parameters. These methods are useful for queries with large numbers of parameters - though the GString variations are often preferred in such cases too. Reminder: when you see a variant with Object[] as the type of the last parameter, Groovy allows vararg style parameters so you don't explicitly need to create an Object[] and if the first parameter is of type Map, Groovy supports named arguments - examples of both are contained in the examples below.

Named parameter queries use placeholder values in the query String. Two forms are supported ':propname1' and '?.propname2'. For these variations, a single model object is supplied in the parameter list/array/map. The propname refers to a property of that model object. The model object could be a map, Expando or domain class instance. Here are some examples:

 // using rows() with a named parameter with the parameter supplied in a map
 println sql.rows('select * from PROJECT where name=:foo', [foo:'Gradle'])
 // as above for eachRow()
 sql.eachRow('select * from PROJECT where name=:foo', [foo:'Gradle']) {
     // process row
 }

 // an example using both the ':' and '?.' variants of the notation
 println sql.rows('select * from PROJECT where name=:foo and id=?.bar', [foo:'Gradle', bar:40])
 // as above but using Groovy's named arguments instead of an explicit map
 println sql.rows('select * from PROJECT where name=:foo and id=?.bar', foo:'Gradle', bar:40)

 // an example showing rows() with a domain object instead of a map
 class MyDomainClass { def baz = 'Griffon' }
 println sql.rows('select * from PROJECT where name=?.baz', new MyDomainClass())
 // as above for eachRow() with the domain object supplied in a list
 sql.eachRow('select * from PROJECT where name=?.baz', [new MyDomainClass()]) {
     // process row
 }
 

Named ordinal parameter queries have multiple model objects with the index number (starting at 1) also supplied in the placeholder. Only the question mark variation of placeholder is supported. Here are some examples:

 // an example showing the model objects as vararg style parameters (since rows() has an Object[] variant)
 println sql.rows("select * from PROJECT where name=?1.baz and id=?2.num", new MyDomainClass(), [num:30])

 // an example showing the model objects (one domain class and one map) provided in a list
 sql.eachRow("select * from PROJECT where name=?1.baz and id=?2.num", [new MyDomainClass(), [num:30]]) {
     // do something with row
 }
 


*/