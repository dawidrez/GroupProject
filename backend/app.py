import os

from app.routes import film
from database import init_db
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JSON_AS_ASCII"] = (
    False  # Enable proper Unicode character encoding in JSON responses
)

CORS(app)
# Initialize the database
init_db(app)

# Register blueprints
app.register_blueprint(film)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
