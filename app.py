from flask import Flask, render_template, request, session
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = 'HOMEWORK'

@app.route('/', methods=['GET', 'POST'])
def home():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if request.method == 'GET':
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        correct_answer = num1 + num2
        question = f"What is {num1} + {num2}?"
        session['correct_answer'] = correct_answer
        session['question'] = question

        result = None
    else:
        user_answer = request.form['answer']
        correct_answer = session['correct_answer']
        if int(user_answer) == correct_answer:
            result = "Correct! Well done."
        else:
            result = f"Wrong! The correct answer was {correct_answer}. Try again."
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        correct_answer = num1 + num2
        question = f"What is {num1} + {num2}?"
        session['correct_answer'] = correct_answer
        session['question'] = question
    return render_template('index.html', current_time=current_time, question=session['question'], result=result)

def main():
    app.run()

if __name__ == '__main__':
    main()