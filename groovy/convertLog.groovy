import groovy.json.*;

// ---------------------- �ݒ� �������� ---------------------
// ���O�t�@�C���z�u�̃��[�g�f�B���N�g��
def ROOT_DIR = "logs"

// �t�@�C�����i�荞�ސ��K�\��
def FILE_FILTER = /.*\.log/

// ���O�t�@�C�������o�͂���
def OUTPUT_LOGFILE_NAME = true

// ���O�̓��������[�J���^�C���ɕϊ�����
def CONV_LOCAL_TIME = true

// ���O�̓����t�H�[�}�b�g�i���[�J���^�C���ɕϊ�����ꍇ�̂ݎg�p�j
def LOG_DATE_FORMAT = "yyyy-MM-dd'T'HH:mm:ssX"

// �o�͂���ۂ̓����t�H�[�}�b�g�i���[�J���^�C���ɕϊ�����ꍇ�̂ݎg�p�j
def OUTPUT_DATE_FORMAT = "yyyy/MM/dd HH:mm:ss" 

// �o�͂���ۂ̊e���ڂ̋�؂蕶��
def OUTPUT_DELIM = "\t"

// ���o���郍�O���x���i�v�f������Ώ����j
def FILTER_LEVEL = [] // ["ERROR", "WARN"]

// �s�ԍ����o�͂���
def OUTPUT_ROW_NUMBER = true

// �� �o�͂��鍀�ڂ̑I���ƕ��ёւ��́A�X�N���v�g����ҏW���Ă��������B

// ---------------------- �ݒ� �����܂� ---------------------

def fopen(path = ".") { new File(path); }

def getFiles(dir, filter) { dir.listFiles().findAll{ filter ? it.name ==~ filter : true }.sort{ it.lastModified() }}

def slurper = new JsonSlurper()

def processFiles = { dir ->

	getFiles(dir, FILE_FILTER).each { file ->
		if (OUTPUT_LOGFILE_NAME) println "\nLog File:\t${file.path}"
		
		file.eachLine("UTF-8", { line, rowNum  ->
			def map = [:]
			try {
				map = slurper.parseText(line)
			} catch (JsonException ex) {
				println line 
				return
			}
			
			if (FILTER_LEVEL && !FILTER_LEVEL.contains(map.level)) return
			
			datetime = map.time
			if (CONV_LOCAL_TIME) {
				datetime = Date.parse(LOG_DATE_FORMAT, datetime).format(OUTPUT_DATE_FORMAT, TimeZone.getDefault())
			}
			
			// �o�͂��鍀��
			output_fields = [datetime, map.level, map.message, map.exception?:""]
			
			if (OUTPUT_ROW_NUMBER) {
				output_fields.add(0, String.format("%06d", rowNum));
			}
			
			println output_fields.join(OUTPUT_DELIM)
		})
	} 
}

def rootDir = ROOT_DIR ? fopen(ROOT_DIR) : fopen()
processFiles(rootDir)
rootDir.eachDirRecurse() { processFiles(it) } 

