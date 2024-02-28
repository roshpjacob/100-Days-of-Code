from question_model import Question
from data import question_data
from quiz_brain import Quizzer

question_bank = []

for i in question_data:
    question = Question(i["text"], i["answer"].lower())
    question_bank.append(question)

quiz = Quizzer(question_bank)
for i in range(len(question_bank)):
    quiz.askques()


print(f"\nFINAL SCORE: {quiz.score}/{len(question_bank)}")
if quiz.score == 12:
    print("Excellent! Perfect score")
elif quiz.score >= 9:
    print("Very good effort!")
elif 5 <= quiz.score < 9:
    print("Not bad. Can do better next time!")
else:
    print("Must put in more effort next time!")

