import random

questions = {
    "What is the keyword to define a function in Python?": "def",
    "Which data is used to store True or False values?": "boolean",
    "Which symbol is used to comment in Python?": "#",
    "What function is used to get input from the user?": "input",
    "How do you start a for loop in Python?": "for",
    "What is the output of 2 ** 3 in Python?": "8",
    "What keyword is used to import a module in Python?": "import",
    "What does the len() function return?": "length",
    "What is the result of 10 // 3 in python?": "3"
}

def python_trivia_game():
    questions_list = list(questions.keys())
    total_questions = 1
    score = 0

    selected_questions = random.sample(questions_list, total_questions)
    print(selected_questions)

python_trivia_game()