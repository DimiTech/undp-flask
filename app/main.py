from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# TODO: Create a sensible project structure.
# TODO: Extract the DB related stuff to it's own module.

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://test:test@0.0.0.0:3306/UNDP'

db = SQLAlchemy(app)

# ---------------------------------------------------------------------------------- #
# TODO: This section is only for testing purposes. Delete it.
class Test(db.Model):
    __tablename__ = 'test'
    id = db.Column('id', db.Unicode(36), unique=True, primary_key=True)

tests = Test.query.all()

for test in tests:
    print(test.id)

# ---------------------------------------------------------------------------------- #

@app.route('/')
def index():
    return 'Hello there!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
