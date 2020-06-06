#3.57 to 4.07
from QuizQuestion import Question
#from QuizQuestion import run_test

question_prompt = [
    "What used to be Liverpool original colours?\n(a) Red and green\n(b) blue\n(c) white and ble\n\n",
    "What originally used to be their stadium full capacity in early days\n(a) (15.000)\n(b) 20.000\n(c) 30.000\n\n",
    "What year Liverpool club was couth in a betting scandal?\n(a) 1915\n(b) 1935\n(c) 1965\n\n"
]

questions = [
    Question(question_prompt[0], "c"),
    Question(question_prompt[1], "b"),
    Question(question_prompt[2], "a"),
]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("\n\nYou got " + str(score) + "/" + str(len(questions)) + " correct.")

run_test(questions)
