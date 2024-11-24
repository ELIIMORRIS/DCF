from flask import Flask, render_template, send_from_directory, abort, request, redirect, url_for
import os

from jinja2 import TemplateNotFound

app = Flask(__name__)

# Define the index for your pages
PAGE_CONTENTS = {
    "data_format": "Collect, enter, organise, analyse data into different formats, tables, pie chart bar chart tally chart line graph database and spreadsheet. Qualitative Data Quantitative Data. Discrete data continuous data. Data sources Google Sheets",
    "data_sets": "Construct, refine, interrogate data sets within tables, chart, spreadsheet, and database. Analyse data set. data collection, statistical, survey, average, median, mode, pattern",
    "evaluate_data": "Evaluate data, tables, graphs, labels, units, axes, visualise, accurate, pattern, analysis, digital tools.",
    "spreadsheet_formulae": "Spreadsheet formulae, organising data, analysing, visualising, practical, budget, interactive, arithmetic operations, sum average range min max value, visualising, comparing, results column, functions",
    "break_down_a_problem": "Decomposition, detail, variables, design, functions, abstraction, details.",
    "debugging": "Debugging, detect, correct, errors, instructions, interactive.",
    "identify_repetitions": "Identify repetitions algorithms, repeating, loop, sequence, pattern, simplify instructions.",
    "importance_of_order": "Importance order of statements algorithm, logic, solution, sequence, decomposition, conditional, loop, abstraction, iteration.",
    "instructions_change": "Change instructions different outcome, modify algorithm, iteration repetition, order operations, directions, creative navigation.",
    "instructions_test_ideas": "Create record verbal, written, symbolic instructions, flowchart, communicate, testing, symbols, language, listen, logical, step, points, brief clear diagram.",
    "refining_algorithms": "Refine algorithms flowchart solve problems, loop, Boolean values, formulae. Clear, logical, order, sequence, steps, test, input, error.",
    "computational_thinking": "Computational Thinking problem-solving skills, abstraction, decomposition, pattern, algorithm design.",
    "resources": "Events workshops, technocamps, hardware, CPD."
}

# Centralised headers dictionary
headers = {
    'home': "Data and Computational Thinking",
    'glossary': "Glossary",
    'computational_thinking': "Computational Thinking",
    'data_format': "Formatting Data",
    'evaluate_data': "Extract and Evaluate Information from Data",
    'data_sets': "Data Sets",
    'spreadsheet_formulae': "Spreadsheet Formulae",
    'break_down_a_problem': "Decomposition: Break Down a Problem",
    'debugging': "Debugging: Detect and Correct Mistakes",
    'instructions_test_ideas': "Create and Record Instructions to Test Ideas",
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

@app.route('/glossary')
def glossary():
    glossary_terms = {
        'Abstraction': 'Identifying and focusing on only the important parts needed to solve the problem.',
        'Algorithm': 'A step-by-step procedure for solving a problem or completing a task.',
        'Coding': 'The process of writing instructions that a computer can understand and execute.',
        'Computational Thinking': 'A problem-solving approach that involves breaking down complex problems into smaller parts, designing algorithms, and using data to find solutions.',
        'Data Literacy': 'The ability to understand, interpret, and use data.',
        'Debugging': 'The process of identifying and correcting in instructions or code.',
        'Decomposition': 'Breaking down a complex problem into smaller, more manageable parts.',
        'Digital Footprint': 'The trail of data that people leave behind when they use the internet or other digital technologies.',
        'Iteration': 'Repeating a set of instructions or steps a certain number of times or until a condition is met.',
        'Prototype': 'An early sample or model of a product used to test concepts or processes.',
        'Pseudocode': 'A simple way of describing a set of instructions that does not have to use specific syntax i.e. can be written in plain English.',
        'Recursion': 'Breaking a component down into smaller components using the same function e.g. Imagine telling a story where each part contains a shorter version of the same story, getting simpler each time until it reaches the ending.',
        'Variable': 'A named container for storing a particular value or piece of data.'
    }
    return render_template('glossary.html', glossary=glossary_terms)

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

@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.args.get('q', '').lower()
    results = {}

    if query:
        for page, content in PAGE_CONTENTS.items():
            if query in content.lower():
                results[page] = content

    return render_template('search_results.html', query=query, results=results)

if __name__ == '__main__':
    app.run(debug=True)