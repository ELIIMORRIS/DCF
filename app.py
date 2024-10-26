from flask import Flask, render_template

app = Flask(__name__)

# Home route for landing page
@app.route('/')
def home():
    return render_template('index.html')

# Route for each topic page.  trailing slash '/url/' added for following. if URL accessed w/o trailing slash, Flask will redirect to the canonical URL with the trailing slash
@app.route('/data_literacy/data_format')
def data_format():
    return render_template('data_literacy/data_format.html')

@app.route('/data_literacy/evaluate_data')
def evaluate_data():
    return render_template('data_literacy/evaluate_data.html')

@app.route('/data_literacy/data_sets')
def data_sets():
    return render_template('data_literacy/data_sets.html')

@app.route('/data_literacy/spreadsheet_formulae')
def spreadsheet_formulae():
    return render_template('data_literacy/spreadsheet_formulae.html')

# Routes for 'problem_solving' pages
@app.route('/problem_solving/break_down_a_problem')
def break_down_a_problem():
    return render_template('problem_solving/break_down_a_problem.html')

@app.route('/problem_solving/debugging')
def debugging():
    return render_template('problem_solving/debugging.html')

@app.route('/problem_solving/instructions_test_ideas')
def instructions_test_ideas():
    return render_template('problem_solving/instructions_test_ideas.html')

@app.route('/problem_solving/instructions_change')
def instructions_change():
    return render_template('problem_solving/instructions_change.html')

@app.route('/problem_solving/identify_repetitions')
def identify_repetitions():
    return render_template('problem_solving/identify_repetitions.html')

@app.route('/problem_solving/refining_algorithms')
def refining_algorithms():
    return render_template('problem_solving/refining_algorithms.html')

@app.route('/problem_solving/importance_of_order')
def importance_of_order():
    return render_template('problem_solving/importance_of_order.html')

# Routes for other pages
@app.route('/computational_thinking')
def computational_thinking():
    return render_template('computational_thinking.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

if __name__ == '__main__':
    app.run(debug=True)
