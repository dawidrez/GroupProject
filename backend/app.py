import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from app.routes import film
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.register_blueprint(film)

    app.run(host='0.0.0.0', debug=True)