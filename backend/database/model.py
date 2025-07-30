from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid
db = SQLAlchemy()

class experiments_table(db.Model):
    __tablename__ = 'experiments_table'
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    experiment_name = db.Column(db.String, unique=True, nullable=False)
    brands = db.Column(db.Text, nullable=False)  
    brand_rank_catagory = db.Column(db.Text, nullable=False)
    experiment_time = db.Column(db.DateTime, default=datetime.now, nullable=False)
    results = db.relationship('experiment_results_table', backref='experiment', cascade="all, delete")

class experiment_results_table(db.Model):
    __tablename__ = 'experiment_results_table'
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    experiment_id = db.Column(db.String, db.ForeignKey('experiments_table.id'), nullable=False)
    brand = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    rank = db.Column(db.Float, nullable=False)
    reason = db.Column(db.String, nullable=False)
