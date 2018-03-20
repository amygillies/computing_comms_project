(function() {
	function buildQuiz() {
		// we'll need a place to store the HTML output
		const output = [];

		// for each question...
		wadQuestions.forEach((currentQuestion, questionNumber) => {
			// we'll want to store the list of answer choices
			const answers = [];

			// and for each available answer...
			for (letter in currentQuestion.answers) {
			// ...add an HTML radio button
				answers.push(
					`<label>
					<input type="radio" name="question${questionNumber}" value="${letter}">
					${letter} :
					${currentQuestion.answers[letter]}
					</label>`
				);
			}

			// add this question and its answers to the output
			output.push(
				`<div class="question"> ${currentQuestion.question} </div>
				<div class="answers"> ${answers.join("")} </div>`
			);
		});

		// finally combine our output list into one string of HTML and put it on the page
		quizContainer.innerHTML = output.join("");
	}

	function showResults() {
		// gather answer containers from our quiz
		const answerContainers = quizContainer.querySelectorAll(".answers");

		// keep track of user's answers
		let numCorrect = 0;

		// for each question...
		wadQuestions.forEach((currentQuestion, questionNumber) => {
			// find selected answer
			const answerContainer = answerContainers[questionNumber];
			const selector = `input[name=question${questionNumber}]:checked`;
			const userAnswer = (answerContainer.querySelector(selector) || {}).value;

			// if answer is correct
			if (userAnswer === currentQuestion.correctAnswer) {
				// add to the number of correct answers
				numCorrect++;
			}
		});

		// show number of correct answers out of total
		resultsContainer.innerHTML = `${numCorrect} out of ${myQuestions.length}`;
	}

	const quizContainer = document.getElementById("quiz");
	const resultsContainer = document.getElementById("results");
	const submitButton = document.getElementById("submit");
	const wadQuestions = [
	{
		question: "If you had to upload you’re code onto a github repository, what sequence would you carry out to upload your code to it?",
		answers: {
			a: "push, commit, add, pull",
			b: "pull, commit, push, add",
			c: "push, add, commit, pull",
			d: "pull, add, commit, push"
		},
		correctAnswer: "d"
	},
	{
		question: "Which CSS selector applies to all div tags within the ID called 'green':",
		answers: {
			a: "green blue",
			b: "div #green",
			c: "green div",
			d: "$green div"
		},
		correctAnswer: "b"
	},
	{ 
		question: "Building web applications involves an array of challenges and complexities, these include:", 
		answers: {
			a: "The composition of the development team, the immature and legacy technologies, and the low expectations of users",
			b: "The hypertext structure, the demand by users for instant availability, the variety of device and the different web frameworks",
			c: "The lack of an accepted development methodology, the hypertext structure, the homogeneous user populations",
			d: "The variety of devices, the simplicity of the HTTP protocol, and the composition of the development team"
		},
		correctAnswer: "d"
	},
	{
		question: "What is the role of XML on the web?",
		answers: {
			a: "to describe semi-structured documents, to be a mechanism for sharing, storing and transporting annotated data, and to display data",
			b: "to be mechanism for storing annotated data, to be a mechanism for sharing annotated data, and to be a mechanism for securing annotated data",
			c: "to be mechanism for storing annotated data, to be a mechanism for sharing annotated data, and to display data",
			d: "to describe semi-structure documents, to be a mechanism for transporting annotated data, and to display data"
		},
		correctAnswer: "a"
	},
	{
		question: "Given the HTML code shown below, how would the element be rendered: <p class='quizcode'> &ltp&gt&ltp class=”blue” style=”background-colour: yellow”&gtGoodbye world&lt/p&gt&lt/p&gt </p>",
		answers: {
			a: "Goodbye world, with no border and green background",
			b: "Goodbye world with border and green background",
			c: "Goodbye world with border and yellow background",
			d: "Goodbye world with no border and no background colour",
		},
		correctAnswer: "c"
	},
	{
		question: "Which line of JQuery code selects the element with a class red and assigns an event to when the element is clicked?",
		answers: {
			a: "$(“.red”).click()",
			b: "$(“.red”).onclick()",
			c: "$(“#red”).click()",
			d: "$(“#red”).onclick()"
		},
		correctAnswer: "a"
	},
	{
		question: "When using HTTP, two methods are commonly used. Select the statement that best describes what each method does.",
		answers: {
			a: "POST appends data to the URL as key-value pairs, PUSH sends the data as part of the message",
			b: "PUSH sends the data as part of the message, GET appends data to the URL as key-value pairs",
			c: "GET appends data to the URL as key-value pairs, POST sends data packaged as part of the message",
			d: "GET sends data packaged as part of the message, POST appends data to the URL as key-value pairs"
		},
		correctAnswer: "c"
	},
	{
		question: "In app/models.py, you need to create the models Author and Story. Each Author has a name of up to 128 characters, the number of views and likes are stored, along with author name slug line. The name of each Author needs to be different, i.e. it must be unique. The code for app/models.py is almost complete, but some lines are missing and need to be added in: from django.db import models from django.template.defaultfilters import slugify from django.contrib.auth.models import User class Author(models.Model): name = models.CharField(max_length=128, unique=True) views = models.IntegerField(default=0) likes = models.IntegerField(default=0) <see Question 8>		(P1) def save(self, *args, **kwargs): <see Question 9> 	(P2) super(Category, self).save(*args, **kwargs) class Story(models.Model): <see Question 10>		(P3) title = models.CharField(max_length=128) story_description = models.TextField() views = models.IntegerField(default=0) def __unicode__(self): return self.title. What line of code should be inserted at P1:",
		answer: {
			a: "slug &#61 models.SlugField(default&#61’’,unique=True)",
			b: "slug &#61 models.SlugField(default&#61’’)",
			c: "slug &#61 models.SlugField()",
			d: "slug &#61 models.SlugField(blank=False)"
		},
		correctAnswer: "a"
	},
	{ 
		question: "What line of code should be inserted at P2:",
		answer: {
			a: "slug &#61 slugify(name)",
			b: "self.slug &#61 slugify(name)",
			c: "slug &#61 slugify(self.name)",
			d: "self.slug &#61 slugify(self.name)"
		},
		correctAnswer: "c"
	},
	{
		question: "What line of code should be inserted at P3:",
		answer: {
			a: "author &#61 models.ForeignKeyField(Author)",
			b: "author &#61 models.ForeignKey(Author)",
			c: "story &#61 models.ForeignKey(Story)",
			d: "story &#61 models.ForeignKeyField(Story)"
		},
		correctAnswer: "b"
	}
	];
	

	// display quiz right away
	buildQuiz();

	// on submit, show results
	submitButton.addEventListener("click", showResults);
})();