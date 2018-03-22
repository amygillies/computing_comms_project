function check(){
	
	var question1 = document.cs2tquiz.question1.value;
	var question2 = document.cs2tquiz.question2.value;
	var question3 = document.cs2tquiz.question3.value;
	var question4 = document.cs2tquiz.question4.value;
	var question5 = document.cs2tquiz.question5.value;
	var question6 = document.cs2tquiz.question6.value;
	var question7 = document.cs2tquiz.question7.value;
	var question8 = document.cs2tquiz.question8.value;
	var question9 = document.cs2tquiz.question9.value;
	var question10 = document.cs2tquiz.question10.value;
	
	var correct = 0;
	
	if (question1 == "a") {
		correct++;
	}
	if (question2 == "c") {
		correct++
	}
	if (question3 == "b") {
		correct++
	}
	if (question4 == "d") {
		correct++
	}
	if (question5 == "a") {
		correct++
	}
	if (question6 == "a") {
		correct++
	}
	if (question7 == "c") {
		correct++
	}
	if (question8 == "b") {
		correct++
	}
	if (question9 == "a") {
		correct++
	}
	if (question10 == "c") {
		correct++
	}
	
	document.getElementById("after_submit").style.visibility = "visible";
	document.getElementById("number_correct").innerHTML = "You got " + correct + " correct";
	
}

function checkandsubmit(){
	
	var question1 = document.cs2tquiz.question1.value;
	var question2 = document.cs2tquiz.question2.value;
	var question3 = document.cs2tquiz.question3.value;
	var question4 = document.cs2tquiz.question4.value;
	var question5 = document.cs2tquiz.question5.value;
	var question6 = document.cs2tquiz.question6.value;
	var question7 = document.cs2tquiz.question7.value;
	var question8 = document.cs2tquiz.question8.value;
	var question9 = document.cs2tquiz.question9.value;
	var question10 = document.cs2tquiz.question10.value;
	
	var correct = 0;
	
	if (question1 == "a") {
		correct++;
	}
	if (question2 == "c") {
		correct++
	}
	if (question3 == "b") {
		correct++
	}
	if (question4 == "d") {
		correct++
	}
	if (question5 == "a") {
		correct++
	}
	if (question6 == "a") {
		correct++
	}
	if (question7 == "c") {
		correct++
	}
	if (question8 == "b") {
		correct++
	}
	if (question9 == "a") {
		correct++
	}
	if (question10 == "c") {
		correct++
	}
	
	document.getElementById("after_submit").style.visibility = "visible";
	document.getElementById("correct").value = correct;
	document.getElementById("number_correct").innerHTML = "You got " + correct + " correct";
	
	var r = confirm("You got " + correct + " correct");
	if (r == true) {
		setTimeout(function(){document.getElementById("cs2t_form").submit();}, 2000);
	}
}