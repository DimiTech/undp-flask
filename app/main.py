import uuid

from flask         import Flask
from flask         import request
from flask         import jsonify
from flask_migrate import Migrate

app = Flask(__name__)

from db import db
from db import Application

migrate = Migrate(app, db)

@app.route('/', methods=['GET'])
def index():
    return 'APPLICATION WORKS!'

@app.route('/', methods=['POST'])
def create_new_application():
    new_uuid = str(uuid.uuid4())
    data = request.get_json()
    new_application = Application(
        uuid                       = new_uuid,
        application_type_id        = data['application_type_id'],
        title                      = data['title'],
        relevant_interests         = data['relevant_interests'],
        self_government            = data['self_government'],
        contact_person             = data['contact_person'],
        applicant_website          = data['applicant_website'],
        project_duration_in_months = data['project_duration_in_months'],
        other_applicants           = data['other_applicants'],
        project_summaries          = data['project_summaries'],
        detailed_description       = data['detailed_description'],
        innovation                 = data['innovation'],
        project_activities         = data['project_activities'],
        expected_outcomes          = data['expected_outcomes'],
        gender_approach            = data['gender_approach'],
        project_budget             = data['project_budget']
    )
    db.session.add(new_application)
    db.session.commit()
    
    return jsonify({'uuid': new_uuid}) 

