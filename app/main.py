import os
import uuid

from flask import Flask
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# TODO: Create a sensible project structure.
# TODO: Extract the DB related stuff to it's own module.

MYSQL_HOST = os.getenv('MYSQL_HOST', '127.0.0.1')

DB_CONN_STR = 'mysql+pymysql://test:test@%s:3306/UNDP' % MYSQL_HOST

app.config['SQLALCHEMY_DATABASE_URI']        = DB_CONN_STR
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']  = True

db = SQLAlchemy(app)

migrate = Migrate(app, db)

# --------------------------------------------------------------------------- #

# TODO: Move the models somewhere else.

class ContactPeople(db.Model):
    __tablename__ = 'contact_people'
    person_id = db.Column(
        'person_id', 
        db.Integer,
        unique=True,
        primary_key=True,
        nullable=False
    )
    full_name = db.Column(
        'full_name',
        db.String(255),
        nullable=False
    )
    address = db.Column(
        'address',
        db.String(255),
        nullable=False
    )
    postal_code = db.Column(
        'postal_code',
        db.String(100),
        nullable=False
    )
    e_mail = db.Column(
        'e_mail',
        db.String(100),
        nullable=False
    )
    phone = db.Column(
        'phone',
        db.String(100),
        nullable=False
    )

class Application(db.Model):
    __tablename__ = 'applications'
    application_id = db.Column(
        'application_id', 
        db.Integer,
        unique=True,
        primary_key=True,
        nullable=False
    )
    application_uuid = db.Column(
        'application_uuid', 
        db.Unicode(36),
        unique=True,
        nullable=False
    )
    application_type = db.Column(
        'application_type',
        db.String(50),
        nullable=False
    )
    title = db.Column(
        'title',
        db.String(255),
        nullable=False
    )
    relevant_interests = db.Column(
        'relevant_interests',
        db.Text,
        nullable=False
    )
    self_government = db.Column(
        'self_government',
        db.String(500),
        nullable=False
    )
    contact_person_id = db.Column(
        'contact_person_id', 
        db.Integer,
        nullable=False
    )
    applicant_website = db.Column(
        'applicant_website',
        db.String(2083),
        nullable=False
    )
    project_duration_in_months = db.Column(
        'project_duration_in_months', 
        db.SmallInteger,
        nullable=False
    )
    detailed_description = db.Column(
        'detailed_description',
        db.Text,
        nullable=False
    )
    innovation = db.Column(
        'innovation',
        db.Text,
        nullable=False
    )
    project_activities = db.Column(
        'project_activities',
        db.Text,
        nullable=False
    )
    expected_outcomes = db.Column(
        'expected_outcomes',
        db.Text,
        nullable=False
    )
    gender_approach = db.Column(
        'gender_approach',
        db.Text,
        nullable=False
    )
    project_budget = db.Column(
        'project_budget',
        db.Text,
        nullable=False
    )

# TODO: Add the `application_id` foreign key.

class ProjectSummary(db.Model):
    __tablename__ = 'project_summaries'
    application_id = db.Column(
        'application_id', 
        db.Integer,
        unique=True,
        primary_key=True,
        nullable=False
    )
    summary_id = db.Column(
        'summary_id', 
        db.Integer,
        unique=True,
        primary_key=True,
        nullable=False
    )
    language = db.Column(
        'language', 
        db.Unicode(2),
        nullable=False
    )
    summary = db.Column(
        'summary', 
        db.Text,
        nullable=False
    )

# --------------------------------------------------------------------------- #

@app.route('/', methods=['GET'])
def index():
    return 'APPLICATION WORKS!'

@app.route('/', methods=['POST'])
def test():
    new_uuid = str(uuid.uuid4())
    data = request.get_json()
    new_contact_person = ContactPeople(
        full_name=data['contact_person']['full_name'],
        address=data['contact_person']['address'],
        postal_code=data['contact_person']['postal_code'],
        e_mail=data['contact_person']['e_mail'],
        phone=data['contact_person']['phone'],
    )
    new_application = Application(
        application_uuid=new_uuid,
        application_type=data['application_type'],
        title=data['title'],
        relevant_interests=data['relevant_interests'],
        self_government=data['self_government'],
        contact_person_id=data['contact_person_id'],
        applicant_website=data['applicant_website'],
        project_duration_in_months=data['project_duration_in_months'],
        detailed_description=data['detailed_description'],
        innovation=data['innovation'],
        project_activities=data['project_activities'],
        expected_outcomes=data['expected_outcomes'],
        gender_approach=data['gender_approach'],
        project_budget=data['project_budget']
    )
    db.session.add(new_contact_person)
    db.session.add(new_application)
    db.session.commit()

    new_project_summary_en = ProjectSummary(
        application_id=1, # TODO: Add the newly inserted application ID.
        language='EN',
        summary=data['project_summary_en']['summary']
    )
    new_project_summary_sr = ProjectSummary(
        application_id=1, # TODO: Add the newly inserted application ID.
        language='SR',
        summary=data['project_summary_sr']['summary']
    )
    db.session.add(new_project_summary_en)
    db.session.add(new_project_summary_sr)
    db.session.commit()
    
    return jsonify({'uuid': new_uuid}) 

