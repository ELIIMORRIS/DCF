from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

class Criteria(db.Model):
    __tablename__ = 'lesson_activity' 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)  
    description = db.Column(db.Text, nullable=True)
    dcf_element = db.Column(db.String(100), nullable=True)  
    progression_step = db.Column(db.String(10), nullable=True)
    template_name = db.Column(db.String(35), unique=True, nullable=False)
