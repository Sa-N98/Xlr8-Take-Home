import os

def app_config(app):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    
    # Set the SQLAlchemy database URI
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + \
    os.path.join(current_dir, 'database', "database.sqlite3")

    
