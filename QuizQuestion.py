#from Quiz import questions

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

#def run_test(questions):
    #score = 0
    #for question in questions:
        #answer = input(question.prompt)
        #if answer == question.answer:
            #score += 1
    #print("\n\nYou got " + str(score) + "/" + str(len(questions)) + " correct.")
