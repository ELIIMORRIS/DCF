from flask import Flask, render_template, send_from_directory, abort
import os

app = Flask(__name__)

# Centralised headers dictionary
headers = {
    'home': "Data and Computational Thinking",
    'computational_thinking': "Computational Thinking",
    'data_format': "Formatting Data",
    'evaluate_data': "Extract and Evaluate Information from Data",
    'data_sets': "Data Sets",
    'spreadsheet_formulae': "Spreadsheet Formulae",
    'break_down_a_problem': "Decomposition: Break Down a Problem",
    'debugging': "Debugging: Detect and Correct Mistakes",
    'instructions_test_ideas': "Create + Record Instructions to Test Ideas",
    'instructions_change': "Change Instructions to Achieve a Different Outcome",
    'identify_repetitions': "Identify Repetitions in a Sequence",
    'refining_algorithms': "Refining Algorithms",
    'importance_of_order': "Importance of Order of Statements within Algorithms",
    'resources': "Resources"
}

# Context processor to make headers dictionary available globally
@app.context_processor
def inject_headers():
    return dict(headers=headers)

# Home route for landing page
@app.route('/')
def home():
    return render_template('index.html', header=headers['home'])

# Route for each topic page.  trailing slash '/url/' added for following. if URL accessed w/o trailing slash, Flask will redirect to the canonical URL with the trailing slash
@app.route('/data_literacy/data_format')
def data_format():
    return render_template('data_literacy/data_format.html', header=headers['data_format'], color="#E67E22")

@app.route('/data_literacy/evaluate_data')
def evaluate_data():
    return render_template('data_literacy/evaluate_data.html', header=headers['evaluate_data'], color="#E67E22")

@app.route('/data_literacy/data_sets')
def data_sets():
    return render_template('data_literacy/data_sets.html', header=headers['data_sets'], color="#E67E22")

@app.route('/data_literacy/spreadsheet_formulae')
def spreadsheet_formulae():
    return render_template('data_literacy/spreadsheet_formulae.html', header=headers['spreadsheet_formulae'], color="#E67E22")

# Routes for 'problem_solving' pages
@app.route('/problem_solving/break_down_a_problem')
def break_down_a_problem():
    return render_template('problem_solving/break_down_a_problem.html', header=headers['break_down_a_problem'], color="#00AB66")

@app.route('/problem_solving/debugging')
def debugging():
    return render_template('problem_solving/debugging.html', header=headers['debugging'], color="#00AB66")

@app.route('/problem_solving/instructions_test_ideas')
def instructions_test_ideas():
    return render_template('problem_solving/instructions_test_ideas.html', header=headers['instructions_test_ideas'], color="#00AB66")

@app.route('/problem_solving/instructions_change')
def instructions_change():
    return render_template('problem_solving/instructions_change.html', header=headers['instructions_change'], color="#00AB66")

@app.route('/problem_solving/identify_repetitions')
def identify_repetitions():
    return render_template('problem_solving/identify_repetitions.html', header=headers['identify_repetitions'], color="#00AB66")

@app.route('/problem_solving/refining_algorithms')
def refining_algorithms():
    return render_template('problem_solving/refining_algorithms.html', header=headers['refining_algorithms'], color="#00AB66")

@app.route('/problem_solving/importance_of_order')
def importance_of_order():
    return render_template('problem_solving/importance_of_order.html', header=headers['importance_of_order'], color="#00AB66")

# Routes for other pages
@app.route('/computational_thinking')
def computational_thinking():
    return render_template('computational_thinking.html', header=headers['computational_thinking'])

@app.route('/download/<filename>')
def download_file(filename):
    downloads_dir = 'static/downloads'
    # Ensure the file exists in the directory
    if os.path.isfile(os.path.join(downloads_dir, filename)):
        return send_from_directory(downloads_dir, filename, as_attachment=True)
    else:
        abort(404)  # Return a 404 if the file does not exist

@app.route('/resources')
def resources():
    return render_template('resources.html', header=headers['resources'])

if __name__ == '__main__':
    app.run(debug=True)