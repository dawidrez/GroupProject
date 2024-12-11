import os
from flask import Flask
from dotenv import load_dotenv
from app.routes import film
from database import db, init_db

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the database
init_db(app)

# Register blueprints
app.register_blueprint(film)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)