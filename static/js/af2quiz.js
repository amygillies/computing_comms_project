function check(){
	
	var question1 = document.af2quiz.question1.value;
	var question2 = document.af2quiz.question2.value;
	var question3 = document.af2quiz.question3.value;
	var question4 = document.af2quiz.question4.value;
	var question5 = document.af2quiz.question5.value;
	var question6 = document.af2quiz.question6.value;
	var question7 = document.af2quiz.question7.value;
	var question8 = document.af2quiz.question8.value;
	var question9 = document.af2quiz.question9.value;
	var question10 = document.af2quiz.question10.value;
	
	var correct = 0;
	
	if (question1 == "b") {
		correct++;
	}
	if (question2 == "a") {
		correct++
	}
	if (question3 == "c") {
		correct++
	}
	if (question4 == "c") {
		correct++
	}
	if (question5 == "b") {
		correct++
	}
	if (question6 == "d") {
		correct++
	}
	if (question7 == "a") {
		correct++
	}
	if (question8 == "c") {
		correct++
	}
	if (question9 == "d") {
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
		setTimeout(function(){document.getElementById("af2_form").submit();}, 2000);
	}
}