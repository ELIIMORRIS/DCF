from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

class LessonActivity(db.Model):
    __tablename__ = 'lesson_activity' 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)  
    description = db.Column(db.Text, nullable=True)
    dcf_element = db.Column(db.String(100), nullable=True)  
    progression_step = db.Column(db.String(10), nullable=True)
    template_name = db.Column(db.String(35), unique=True, nullable=False)

class UserProgress(db.Model):
    __tablename__ = 'user_progress'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False) 
    activity_id = db.Column(db.Integer, db.ForeignKey('lesson_activity.id'), nullable=False)
    completed = db.Column(db.Boolean, default=False, nullable=False)

    # Optional: Define relationship for easier access to activity details
    activity = db.relationship('LessonActivity', backref=db.backref('user_progress', lazy=True))