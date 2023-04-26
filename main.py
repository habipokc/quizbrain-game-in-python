from question_model import Questions
from data import question_data
from quiz_brain import  QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Questions(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.new_question()

print("You have complete the quiz")
print(f"your final score is {quiz.score}/{len(question_bank)}")



