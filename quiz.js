function promptNumberOfQuestions() {
  const numberOfQuestions = parseInt(prompt("How many questions do you want to answer?"));
  if (!isNaN(numberOfQuestions) && numberOfQuestions > 0) {
    return numberOfQuestions;
  }
  return 0;
}

function initializeQuiz(numberOfQuestions) {
  // Fetch Questions/Answers
  fetch('quiz_data.json')
    .then(response => response.json())
    .then(data => {
      const questionContainer = document.getElementById('question-container');
      const questionElement = document.getElementById('question');
      const optionsElement = document.getElementById('options');
      const submitButton = document.getElementById('submit-btn');
      let currentQuestionIndex = 0;
      let score = 0;

      // Filter the questions based on the desired number
      const filteredQuestions = data.questions.slice(0, numberOfQuestions);

      // Display the current question
      function displayQuestion() {
        const currentQuestion = filteredQuestions[currentQuestionIndex];
        questionElement.textContent = currentQuestion.prompt;

        optionsElement.innerHTML = ''; // Clear previous options

        currentQuestion.choices.forEach((choice, index) => {
          const li = document.createElement('li');
          const input = document.createElement('input');
          input.type = (currentQuestion.type === 'single' || currentQuestion.choices.length === 1) ? 'radio' : 'checkbox';
          input.name = 'option';
          input.value = index;
          li.appendChild(input);
          li.appendChild(document.createTextNode(choice));
          optionsElement.appendChild(li);
        });
      }

      // Calculate and display the score
      function showScore() {
        questionContainer.innerHTML = `<h2>Your Score: ${score} out of ${filteredQuestions.length}</h2>`;
      }

      // Event listener for submit button click
      submitButton.addEventListener('click', () => {
        const selectedOptions = Array.from(document.querySelectorAll('input[name="option"]:checked'))
          .map(input => parseInt(input.value));

        const currentQuestion = filteredQuestions[currentQuestionIndex];

        if (arraysEqual(selectedOptions, currentQuestion.correct_answers)) {
          score++;
        }

        currentQuestionIndex++;

        if (currentQuestionIndex >= filteredQuestions.length) {
          showScore();
        } else {
          displayQuestion();
        }
      });

      // Check if two arrays are equal
      function arraysEqual(arr1, arr2) {
        if (arr1.length !== arr2.length) return false;
        for (let i = 0; i < arr1.length; i++) {
          if (arr1[i] !== arr2[i]) return false;
        }
        return true;
      }

      // Start the quiz
      displayQuestion();
    });
}

// Prompt for the number of questions
const numberOfQuestions = promptNumberOfQuestions();
if (numberOfQuestions > 0) {
  initializeQuiz(numberOfQuestions);
} else {
  alert("Please enter a valid number of questions.");
}
