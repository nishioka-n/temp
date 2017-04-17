
var URL = 'http://outlook.com/';
var userid = '';
var passwd = '';

main();
function main() {
  var ie = new ActiveXObject("InternetExplorer.Application");
  ie.visible = true;
  ie.navigate(URL);
  while( (ie.Busy) || (ie.readystate != 4) ) {
    WScript.Sleep(100);
  }
  
  //var f = ie.document.forms[0];
  var doc = ie.document;
  
  // ユーザID
  doc.getElementById('login').value = userid;
  // パスワード
  doc.getElementById('passwd').value = passwd;
  
  doc.getElementById('SI').click();
  
  
}