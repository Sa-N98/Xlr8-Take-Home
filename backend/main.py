from flask import Flask
from flask_cors import CORS
import os
from config import app_config
from database.model import db
from routes.test_rout import test_route
from routes.ai_agent import ai_bot_route 
from routes.dashbord import dashbord_cards
current_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app_config(app)
db.init_app(app)
CORS(app, origins=["https://xlr8-brand-ranker.onrender.com"])
app.app_context().push()


@app.route("/")
def home():
    return "Hello, Flask!"

test_route(app)
ai_bot_route(app)
dashbord_cards(app)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
