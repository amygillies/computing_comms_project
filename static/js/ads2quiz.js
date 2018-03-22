function check(){
	
	var question1 = document.ads2quiz.question1.value;
	var question2 = document.ads2quiz.question2.value;
	var question3 = document.ads2quiz.question3.value;
	var question4 = document.ads2quiz.question4.value;
	var question5 = document.ads2quiz.question5.value;
	var question6 = document.ads2quiz.question6.value;
	var question7 = document.ads2quiz.question7.value;
	var question8 = document.ads2quiz.question8.value;
	var question9 = document.ads2quiz.question9.value;
	var question10 = document.ads2quiz.question10.value;
	
	var correct = 0;
	
	if (question1 == "c") {
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
	if (question7 == "b") {
		correct++
	}
	if (question8 == "c") {
		correct++
	}
	if (question9 == "b") {
		correct++
	}
	if (question10 == "d") {
		correct++
	}
	
	document.getElementById("after_submit").style.visibility = "visible";
	document.getElementById("number_correct").innerHTML = "You got " + correct + " correct";
	
}

function checkandsubmit(){
	
	var question1 = document.ads2quiz.question1.value;
	var question2 = document.ads2quiz.question2.value;
	var question3 = document.ads2quiz.question3.value;
	var question4 = document.ads2quiz.question4.value;
	var question5 = document.ads2quiz.question5.value;
	var question6 = document.ads2quiz.question6.value;
	var question7 = document.ads2quiz.question7.value;
	var question8 = document.ads2quiz.question8.value;
	var question9 = document.ads2quiz.question9.value;
	var question10 = document.ads2quiz.question10.value;
	
	var correct = 0;
	
	if (question1 == "c") {
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
	if (question7 == "b") {
		correct++
	}
	if (question8 == "c") {
		correct++
	}
	if (question9 == "b") {
		correct++
	}
	if (question10 == "d") {
		correct++
	}
	
	document.getElementById("after_submit").style.visibility = "visible";
	document.getElementById("correct").value = correct;
	document.getElementById("number_correct").innerHTML = "You got " + correct + " correct";
	
	var r = confirm("You got " + correct + " correct");
	if (r == true) {
		setTimeout(function(){document.getElementById("ads2_form").submit();}, 2000);
	}
}