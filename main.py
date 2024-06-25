from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        grades = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1}
        total_points = 0
        total_grade = 0
        num_subjects = len([key for key in request.form.keys() if key.startswith('Subject')])

        for i in range(1, num_subjects + 1):
            subject = request.form[f'Subject{i}']
            points = request.form[f'Points{i}']
            grade = request.form[f'Grade{i}']

            # Check if fields are empty
            if not points or not grade:
                return render_template('index.html', error='All fields are required for each subject.')

            points = float(points)

            if grade not in grades:
                return render_template('index.html', error=f'Invalid grade entered for Subject {i}. Please use A, B, C, D, or E.')

            grade = grades[grade]

            total_points += points
            total_grade += points * grade

        if total_points == 0:
            return render_template('index.html', error='Total points cannot be zero')
        else:
            average = total_grade / total_points
            return render_template('index.html', average=average)
    except ValueError:
        return render_template('index.html', error='Invalid input. Please enter valid numbers.')

if __name__ == '__main__':
    app.run(debug=True)
