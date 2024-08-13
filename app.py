from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Set up the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('postgresql://render_1_ssjk_user:wwuDljEgJ5HoCD0D5HrCfBf5YK6crvCp@dpg-cqtd6raj1k6c738j8g30-a.oregon-postgres.render.com/render_1_ssjk', 'sqlite:///local.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a simple model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Define a simple route
@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
