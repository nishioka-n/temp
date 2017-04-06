/*
 * �^�C���X�^���v��t���ăt�@�C�����R�s�[
 */
/* ---------- �ݒ� ---------- */
// �^�C���X�^���v���t�@�C���̍X�V��������擾����Bfalse �̏ꍇ�A���ݎ����B
var FILE_TIMESTAMP = true;

// �R�s�[��ǎ��p�ɃZ�b�g����B
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
 * �w�肵���p�X�̃t�@�C�����^�C���X�^���v�t�ŃR�s�[
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
 * �R�}���h���C�������̎擾�iJavaScript�̔z��֓���ւ��j
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
 * ��ʏo��
 */
function println(msg) {
    WScript.echo(msg);
}

/**
 * �^�C���X�^���v������̐���
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