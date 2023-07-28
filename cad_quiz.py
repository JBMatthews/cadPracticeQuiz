import json
import random

# Function to present a question and check the answer
def present_question(question_data):
    prompt = question_data['prompt']
    choices = question_data['choices']
    correct_answers = question_data['correct_answers']

    print(prompt)
    print("Choices:")
    for i, choice in enumerate(choices):
        print(f"{i + 1}. {choice}")

    user_answer = input("Enter the number(s) of the correct choice(s) (comma-separated): ")
    user_answer = user_answer.split(',')

    # Convert user's answer to corresponding choices
    user_choices = [choices[int(answer) - 1] for answer in user_answer if answer.isdigit() and int(answer) <= len(choices)]


    # Check if the user's answer matches the correct answer(s)
    if set(user_choices) == set(correct_answers):
        print("Correct!")
        return True
    else:
        print("Incorrect!")
        print(f"The correct answer(s) is/are: {', '.join([choices[int(answer) - 1] for answer in correct_answers if answer.isdigit()])}")
        return False

# Function to administer the quiz
def administer_quiz(quiz_data, num_questions):
    score = 0
    total_questions = min(num_questions, len(quiz_data))
    correct_answers = []

    print("Welcome to CAD Quiz!")
    print("====================")

    # Randomize the order of questions
    randomized_quiz_data = random.sample(quiz_data, len(quiz_data))

    # Iterate over each question in the randomized quiz data
    for i, question in enumerate(randomized_quiz_data[:num_questions], start=1):
        print(f"\nQuestion {i}/{total_questions}:")
        if present_question(question):
            score += 1
        else:
            correct_answers.append(i)

    # Print the final score
    print("============================")
    print("Quiz Complete!")
    print(f"Your Score: {score}/{total_questions}")

    # Print the correct answers
    if correct_answers:
        print("\nCorrect Answers:")
        for question_number in correct_answers:
            question = randomized_quiz_data[question_number - 1]
            correct_choices = [str(i + 1) + '. ' + choice for i, choice in enumerate(question['choices']) if i in map(int, question['correct_answers'])]
            print(f"Question {question_number}: {', '.join(correct_choices)}")

# Load the quiz data from a JSON file
with open('quiz_data.json', 'r') as file:
    quiz_data = json.load(file)

# Prompt the user for the number of questions
num_questions = int(input("How many questions would you like to answer? "))

# Administer the quiz
administer_quiz(quiz_data, num_questions)
