from flask import Flask, render_template, send_from_directory, abort, request
from flask_sqlalchemy import SQLAlchemy
import os

from jinja2 import TemplateNotFound
from models import db, Criteria

app = Flask(__name__)

# Set up your database configuration here
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Update the path as needed
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)

# Create the database tables if they do not already exist
with app.app_context():
    db.create_all()  # This creates all tables defined in your models

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
        'Algorithm': 'A step-by-step procedure for solving a problem or accomplishing a task.',
        'Debug': 'The process of identifying and fixing bugs or errors in a program.',
        'Iteration': 'Repeating a set of instructions or steps a certain number of times or until a condition is met.',
        'Prototype': 'An early sample or model of a product used to test concepts or processes.',
        'Computational Thinking': 'A problem-solving process that involves decomposition, pattern recognition, abstraction, and algorithm design.',
        'Decomposition': 'Breaking down a complex problem into smaller, more manageable parts.',
        'Abstraction': 'The process of simplifying complex systems by focusing on the important details and ignoring the irrelevant ones.',
        'Recursion': 'Breaking a component down into smaller components using the same function e.g. Imagine telling a story where each part contains a shorter version of the same story, getting simpler each time until it reaches the ending.',
        'Pseudocode': 'A simple way of describing a set of instructions that does not have to use specific syntax i.e. can be written in plain English.',
        'Variable': 'A named container for a particular value or piece of data.'
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

@app.route('/activities', methods=['GET', 'POST'])
def activities():
    # Get search query from URL parameters, default to empty string if not provided
    search_query = request.args.get('search', '')  
    # Get filter query from URL parameters, default to empty string if not provided
    filter_query = request.args.get('filter', '')

    # Start with a query to get all activities
    activities = Criteria.query

    # Apply search filter if search query is provided
    if search_query:
        activities = activities.filter(Criteria.title.contains(search_query))

    # Apply filter if a filter query is provided
    if filter_query:
        activities = activities.filter(Criteria.dcf_element == filter_query)

    # Get all the filtered activities
    activities = activities.all()

    # Pass filtered activities to the template for rendering
    return render_template('activities.html', activities=activities)

@app.route('/<string:dcf_element>/<string:template_name>')
def activity_detail(dcf_element, template_name):
    activity = Criteria.query.filter_by(template_name=template_name).first_or_404()
    return render_template(f'{dcf_element}/{template_name}.html', activity=activity)

if __name__ == '__main__':
    app.run(debug=True)