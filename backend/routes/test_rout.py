from flask import Flask
import json
from datetime import datetime
from database.model import *



def test_route(app):
    @app.route('/test')
    def test():

        # Step 1: Dummy input
        brands = ["Toyota", "BMW", "Hyundai"]
        categories = ["Fuel Efficiency", "Luxury Features"]

        # Step 2: Create a dummy experiment
        dummy_experiment = experiments_table(
            experiment_name="Test Experiment Cars",
            brands=json.dumps(brands),
            brand_rank_catagory=json.dumps(categories),
            experiment_time=datetime.now()
        )

        db.session.add(dummy_experiment)
        db.session.commit()  # Save to generate experiment.id


        # Step 3: Dummy LLM-style parsed results
        # For both categories, rank the same brands differently
        dummy_results = [
            {"brand": "Hyundai", "category": "Fuel Efficiency", "rank": 1, "reason": "Excellent mileage and hybrid options."},
            {"brand": "Toyota", "category": "Fuel Efficiency", "rank": 2, "reason": "Reliable performance with decent efficiency."},
            {"brand": "BMW", "category": "Fuel Efficiency", "rank": 3, "reason": "Luxury design compromises fuel economy."},

            # Luxury Features
            {"brand": "BMW", "category": "Luxury Features", "rank": 1, "reason": "High-end interiors and advanced tech."},
            {"brand": "Toyota", "category": "Luxury Features", "rank": 2, "reason": "Premium trims offer solid features."},
            {"brand": "Hyundai", "category": "Luxury Features", "rank": 3, "reason": "Affordable features, but not premium."}
        ]

        # Step 4: Insert results into the database
        for r in dummy_results:
            result = experiment_results_table(
                experiment_id=dummy_experiment.id,
                brand=r["brand"],
                category=r["category"],
                rank=r["rank"],
                reason=r["reason"]
            )
            db.session.add(result)

        db.session.commit()
        return "This is a test route!"