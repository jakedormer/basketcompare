var timesClicked = 0

var exVat = document.getElementsByClassName("exVat");
for (var i=0, i< exVat.length; i++){
    exVat[i].style.display = "none";
}


function myFunction() {
        var exVat = document.getElementsByClassName("exVat");
        var incVat = document.getElementsByClassName("incVat") //divsToHide is an array
        timesClicked++;
    for (var i = 0; i < exVat.length; i++){
    	if (timesClicked%2 == 0) {
    		incVat[i].style.display = "table-cell";
    		exVat[i].style.display = "none";
    	} else {
    		incVat[i].style.display = "none";
    		exVat[i].style.display = "table-cell";
    	}
}
}
