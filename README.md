# quizbrain-game-in-python

This code block creates a simple quiz game. It starts by importing two modules: Questions from question_model.py, and QuizBrain from quiz_brain.py. It also imports a list of questions and answers from a data.py module, which contains a list of dictionaries.

The code then creates an empty question_bank list, which will be populated with Questions objects for each question in the question_data list. This is achieved by iterating through each dictionary in the question_data list and extracting the question text and answer. A new Questions object is then created using the question_text and question_answer variables, and added to the question_bank list.

Once the question_bank is populated, the code creates a QuizBrain object called quiz, passing in the question_bank list as an argument. The while loop runs as long as there are still questions left in the quiz, calling the new_question() method of the QuizBrain object on each iteration.

After the loop completes, the code displays a message indicating that the quiz has been completed, and the user's final score is displayed by calling the score and len() methods of the QuizBrain object.
