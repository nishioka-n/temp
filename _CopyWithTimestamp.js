/*
 * タイムスタンプを付けてファイルをコピー
 */
/* ---------- 設定 ---------- */
// タイムスタンプをファイルの更新日時から取得する。false の場合、現在時刻。
var FILE_TIMESTAMP = true;

// コピー後読取専用にセットする。
var SET_READONLY = true;

/* -------------------------- */


var fso = new ActiveXObject('Scripting.FileSystemObject');
var args = getArgs();

main(args);

function main(args) {

    if (args.length == 0) {
        return;
    }

    for (var i = 0; i < args.length; i++) {
        copyWithTimestamp(args[i]);
    }

} // end main


/** 
 * 指定したパスのファイルをタイムスタンプ付でコピー
 */

function copyWithTimestamp(path) {

    if (!fso.FileExists(path)) {
        return;
    }

    var dirName = fso.GetParentFolderName(path);
    var baseName = fso.GetBaseName(path);
    var extention = fso.GetExtensionName(path);

    var dt = new Date();
    if (FILE_TIMESTAMP) {
        var ts = fso.getFile(path).DateLastModified;
        dt = new Date(ts);
    }
    var copyFileName = baseName + '_' + getTimestampString(dt) + '.' + extention;
    var copyFullPath = fso.BuildPath(dirName, copyFileName);

    if (fso.FileExists(copyFullPath)) {
        return;
    }

    fso.CopyFile(path, copyFullPath);

    if (SET_READONLY) {
        fso.GetFile(copyFullPath).Attributes = 1; // ReadOnly
    }
}


/**
 * コマンドライン引数の取得（JavaScriptの配列へ入れ替え）
 */
function getArgs() {

    var argsObj = WScript.Arguments;
    var args = new Array();

    args.length = argsObj.length;

    for (var i = 0; i < args.length; i++) {
        args[i] = argsObj(i);
    }

    return args;
}

/**
 * 画面出力
 */
function println(msg) {
    WScript.echo(msg);
}

/**
 * タイムスタンプ文字列の生成
 */
function getTimestampString(dt) {

    var yy = dt.getFullYear();
    var mm = dt.getMonth() + 1;
    var dd = dt.getDate();
    var hh = dt.getHours();
    var mi = dt.getMinutes();
    var ss = dt.getSeconds();

    var ts = '' + yy;
    var nums = [mm, dd, hh, mi, ss];
    for (var i = 0; i < nums.length; i++) {
        ts += ((nums[i] < 10) ? '0' + nums[i] : nums[i]);
    }

    return ts;
}