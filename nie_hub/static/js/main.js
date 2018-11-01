function category_change(){
	var category = document.getElementById("category").value;
	var sem = document.getElementById("sem");
	
	if(category == "teacher"){				
		sem.disabled = true;
	}else{
		sem.disabled = false;
	}
}