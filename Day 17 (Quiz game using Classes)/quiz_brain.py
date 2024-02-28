class Quizzer:
    def __init__(self, question_bank):
        self.ques_no = 0
        self.qlist = question_bank
        self.score = 0

    def askques(self):
        question = self.qlist[self.ques_no]
        print(f"Q.{self.ques_no+1}: {question.question} (True/False)?  ")
        choice = input().lower()
        self.check_answer(choice, question)

    def check_answer(self, user_answer, question):
        if user_answer == question.answer:
            self.score += 1
            print("You got it right")
            print(f"Current score: {self.score}/{self.ques_no + 1}")

        else:
            print("Wrong Answer!")
            print(f"Current Score: {self.score}/{self.ques_no + 1}\n")

        self.ques_no += 1

