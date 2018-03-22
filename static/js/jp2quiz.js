function check(){
	
	var question1 = document.jp2quiz.question1.value;
	var question2 = document.jp2quiz.question2.value;
	var question3 = document.jp2quiz.question3.value;
	var question4 = document.jp2quiz.question4.value;
	var question5 = document.jp2quiz.question5.value;
	var question6 = document.jp2quiz.question6.value;
	var question7 = document.jp2quiz.question7.value;
	var question8 = document.jp2quiz.question8.value;
	var question9 = document.jp2quiz.question9.value;
	var question10 = document.jp2quiz.question10.value;
	
	var correct = 0;
	
	if (question1 == "c") {
		correct++;
	}
	if (question2 == "c") {
		correct++
	}
	if (question3 == "a") {
		correct++
	}
	if (question4 == "c") {
		correct++
	}
	if (question5 == "a") {
		correct++
	}
	if (question6 == "b") {
		correct++
	}
	if (question7 == "c") {
		correct++
	}
	if (question8 == "d") {
		correct++
	}
	if (question9 == "a") {
		correct++
	}
	if (question10 == "b") {
		correct++
	}
	
	document.getElementById("after_submit").style.visibility = "visible";
	document.getElementById("number_correct").innerHTML = "You got " + correct + " correct";
	
}

function checkandsubmit() {
	
		
	var question1 = document.jp2quiz.question1.value;
	var question2 = document.jp2quiz.question2.value;
	var question3 = document.jp2quiz.question3.value;
	var question4 = document.jp2quiz.question4.value;
	var question5 = document.jp2quiz.question5.value;
	var question6 = document.jp2quiz.question6.value;
	var question7 = document.jp2quiz.question7.value;
	var question8 = document.jp2quiz.question8.value;
	var question9 = document.jp2quiz.question9.value;
	var question10 = document.jp2quiz.question10.value;
	
	var correct = 0;
	
	if (question1 == "c") {
		correct++;
	}
	if (question2 == "c") {
		correct++
	}
	if (question3 == "a") {
		correct++
	}
	if (question4 == "c") {
		correct++
	}
	if (question5 == "a") {
		correct++
	}
	if (question6 == "b") {
		correct++
	}
	if (question7 == "c") {
		correct++
	}
	if (question8 == "d") {
		correct++
	}
	if (question9 == "a") {
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
		setTimeout(function(){document.getElementById("jp2_form").submit();}, 2000);
	}
}
