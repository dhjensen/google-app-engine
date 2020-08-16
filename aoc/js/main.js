function coordUpdate(e) {
	
	var pic = document.getElementById("pic");
	var mIcon = document.getElementById("coord");
	
	var scrLeft = document.documentElement.scrollLeft ? document.documentElement.scrollLeft : document.body.scrollLeft;	
	var scrTop = document.documentElement.scrollTop ? document.documentElement.scrollTop : document.body.scrollTop;
	
	var mouseX = e.clientX + scrLeft;
	var mouseY = e.clientY + scrTop;

	var mPicX = mouseX - pic.offsetLeft;
	var mPicY = mouseY - pic.offsetTop;
	
	mIcon.style.left = (mouseX+10) + 'px';
	mIcon.style.top = mouseY + 'px';
	mIcon.innerHTML = "X " + mPicX + ",Y " + (pic.height - mPicY);
	//mIcon.innerHTML = "Scoll top: " + document.documentElement.scrollTop;
	
}

function coordOver() {
	var elm = document.getElementById("coord");
	elm.style.display = 'block';
	document.body.style.cursor = 'crosshair'
}

function coordOut() {
	var elm = document.getElementById("coord");
	elm.style.display = 'none';	 	
	document.body.style.cursor = 'default'
}