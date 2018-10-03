var timesClicked = 0

function myFunction() {
        var exVat = document.getElementsByClassName("exVat");
        var incVat = document.getElementsByClassName("incVat");
        var vatButton = document.getElementById('vat-button')
        timesClicked++;
    for (var i = 0; i < exVat.length; i++){
    	if (timesClicked%2 == 0) {
    		incVat[i].style.display = "table-cell";
    		exVat[i].style.display = "none";
            vatButton.innerHTML = "inc Vat";
    	} else {
    		incVat[i].style.display = "none";
    		exVat[i].style.display = "table-cell";
            vatButton.innerHTML = "ex Vat";
    	}
}
}

$('[data-toggle="popover"]').popover(); 