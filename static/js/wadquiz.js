function check(){
	
	var question1 = document.wadquiz.question1.value;
	var question2 = document.wadquiz.question2.value;
	var question3 = document.wadquiz.question3.value;
	var question4 = document.wadquiz.question4.value;
	var question5 = document.wadquiz.question5.value;
	var question6 = document.wadquiz.question6.value;
	var question7 = document.wadquiz.question7.value;
	var question8 = document.wadquiz.question8.value;
	var question9 = document.wadquiz.question9.value;
	var question10 = document.wadquiz.question10.value;
	
	var correct = 0;
	
	if (question1 == "d") {
		correct++;
	}
	if (question2 == "b") {
		correct++
	}
	if (question3 == "d") {
		correct++
	}
	if (question4 == "a") {
		correct++
	}
	if (question5 == "c") {
		correct++
	}
	if (question6 == "a") {
		correct++
	}
	if (question7 == "c") {
		correct++
	}
	if (question8 == "a") {
		correct++
	}
	if (question9 == "c") {
		correct++
	}
	if (question10 == "b") {
		correct++
	}
	
	document.getElementById("after_submit").style.visibility = "visible";
	document.getElementById("number_correct").innerHTML = "You got " + correct + " correct";
	
}

function checkandsubmit() {
	
	var question1 = document.wadquiz.question1.value;
	var question2 = document.wadquiz.question2.value;
	var question3 = document.wadquiz.question3.value;
	var question4 = document.wadquiz.question4.value;
	var question5 = document.wadquiz.question5.value;
	var question6 = document.wadquiz.question6.value;
	var question7 = document.wadquiz.question7.value;
	var question8 = document.wadquiz.question8.value;
	var question9 = document.wadquiz.question9.value;
	var question10 = document.wadquiz.question10.value;
	
	var correct = 0;
	
	if (question1 == "d") {
		correct++;
	}
	if (question2 == "b") {
		correct++
	}
	if (question3 == "d") {
		correct++
	}
	if (question4 == "a") {
		correct++
	}
	if (question5 == "c") {
		correct++
	}
	if (question6 == "a") {
		correct++
	}
	if (question7 == "c") {
		correct++
	}
	if (question8 == "a") {
		correct++
	}
	if (question9 == "c") {
		correct++
	}
	if (question10 == "b") {
		correct++
	}
	
	document.getElementById("after_submit").style.visibility = "visible";
	document.getElementById("correct").value = correct;
	document.getElementById("number_correct").innerHTML = "You got " + correct + " correct";
	
	var r = confirm("You got " + correct + " correct");
	if (r == true) {
		setTimeout(function(){document.getElementById("wad2_form").submit();}, 2000);
	}
}