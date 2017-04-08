import static groovy.io.FileType.FILES

def fopen(path = "."){ new File(path) }

def beforeAfteMap = [
 "jp.co":"net."
]

fopen().eachFileRecurse(FILES) { file ->
	
	if (!file.name.endsWith(".java")) return 
	
	def path = file.path
	println path

	def replacedLines = []
	def count = 0
	file.eachLine "UTF-8", { line ->
		def replaced = line
		beforeAfteMap.each { before, after ->
			replaced = replaced.replaceAll(before, after);
		}
		if (line != replaced) {
			println "置換前：\t${line}"
			println "置換後：\t${replaced}"
			count++;
		}
		replacedLines.add replaced
	}
	
	if (!count) return
	
	def back_path = path + ".bak"
	def backup = fopen(back_path)
	if (backup.exists()) {
		backup.delete()
	}
	file.renameTo back_path
	
	fopen(path).withWriter('UTF-8') { writer ->
		replacedLines.each { line ->
    		writer << "$line\r\n"
    	}
    }

} 


