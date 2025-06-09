from flask import Flask, render_template
from models import db, Visit
from dotenv import load_dotenv
import os

load_dotenv()

MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_DB = os.getenv('MYSQL_DB')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}'

db.init_app(app)

@app.route('/')
def index():
    visit = Visit()
    db.session.add(visit)
    db.session.commit()
    count = Visit.query.count()

    return render_template('index.html', count=count)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)