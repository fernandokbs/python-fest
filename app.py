from flask import Flask, render_template
from models import db, Visit

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///visits.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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