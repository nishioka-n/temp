
var xlCSV = 6;

var fso = new ActiveXObject('Scripting.FileSystemObject');

var args = getArgs();

main(args);

function main(args) {

    if (args.length == 0) {
        return;
    }
	
	var excel = new ActiveXObject("Excel.Application");
	excel.Visible = true;
	excel.DisplayAlerts = false;

    for (var i = 0; i < args.length; i++) {
        saveAsCsv(excel, args[i]);
    }
	
	excel.Quit();
}

function saveAsCsv(excel, path) {

	var book = excel.Workbooks.Open(path);

    if (!fso.FileExists(path)) {
        return;
    }

    var dirName = fso.GetParentFolderName(path);
    var baseName = fso.GetBaseName(path);
    var fullPath = fso.BuildPath(dirName, baseName + ".csv");
    
	book.SaveAs(fullPath, xlCSV);
	book.Close();
}

/**
 * コマンドライン引数の取得（JavaScriptの配列へ入れ替え）
 */
function getArgs() {

    var argsObj = WScript.Arguments;
    var args = new Array();

    for (var i = 0; i <argsObj.length; i++) {
        args[i] = argsObj(i);
    }

    return args;
}
