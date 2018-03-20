function check(){
	
	var question1 = document.oose2quiz.question1.value;
	var question2 = document.oose2quiz.question2.value;
	var question3 = document.oose2quiz.question3.value;
	var question4 = document.oose2quiz.question4.value;
	var question5 = document.oose2quiz.question5.value;
	var question6 = document.oose2quiz.question6.value;
	var question7 = document.oose2quiz.question7.value;
	var question8 = document.oose2quiz.question8.value;
	var question9 = document.oose2quiz.question9.value;
	var question10 = document.oose2quiz.question10.value;
	
	var correct = 0;
	
	if (question1 == "b") {
		correct++;
	}
	if (question2 == "d") {
		correct++
	}
	if (question3 == "d") {
		correct++
	}
	if (question4 == "c") {
		correct++
	}
	if (question5 == "a") {
		correct++
	}
	if (question6 == "c") {
		correct++
	}
	if (question7 == "a") {
		correct++
	}
	if (question8 == "d") {
		correct++
	}
	if (question9 == "c") {
		correct++
	}
	if (question10 == "a") {
		correct++
	}
	
	document.getElementById("after_submit").style.visibility = "visible";
	document.getElementById("number_correct").innerHTML = "You got " + correct + " correct";
	
}