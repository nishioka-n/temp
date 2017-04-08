
// 選択テキストの背景色変更
function changeBgColor(color) {
	var selection = getSelection();
	if (selection.rangeCount > 0) {
		var range = selection.getRangeAt(0);
		var newspan = document.createElement('span');
		newspan.style.backgroundColor = color;
		try {
			range.surroundContents(newspan);
		} catch (e) { console.log(e); }
	}
}
function getKeyCode(chr) {
	return chr.charCodeAt(0) - 32;
}
(function() {
	document.onkeydown = function(ev) {
		var kc = ev.keyCode;
		if (kc == getKeyCode("y") ) {
			changeBgColor("yellow");
		} else if (kc == getKeyCode("b") ) {
			changeBgColor("skyblue");
		} else if (getKeyCode("p")) {
			changeBgColor("pink");
		}
	}
})();

void(0);