import uuid

from flask         import Flask
from flask         import request
from flask         import redirect
from flask_migrate import Migrate

app = Flask(__name__)

from db import db
from db import Application

migrate = Migrate(app, db)

@app.route('/challenges/open_data', methods=['POST'])
def create_new_application():
    new_uuid = str(uuid.uuid4())

    print(request.form['title'])
    print(request.form['project_duration_in_months'])
    print(request.files['file_1'])
    print(request.files['file_2'])

    redirect_uri = 'http://%s/success.html?id=%s' % (
        request.remote_addr,
        new_uuid
    )
    return redirect(redirect_uri, code=302)

