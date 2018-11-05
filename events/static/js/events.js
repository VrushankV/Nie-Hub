function buttonChange(){
	value = document.getElementById("sell").value;
	if(value == "No"){
		document.getElementById("sub").value = "SUBMIT";
	}else if(value == "Yes"){
		document.getElementById("sub").value = "NEXT";
	}
}