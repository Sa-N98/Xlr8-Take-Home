from flask import Flask
import json
import requests
from datetime import datetime
from flask_cors import cross_origin
from database.model import *
from flask import request
from ai_agent.bot import ai_call
from datetime import datetime
from database.model import *

def ai_bot_route(app):
    @app.route('/api/rank-brands', methods=['POST'])
    @cross_origin(origin='https://xlr8-brand-ranker.onrender.com/')
    def rank_brands():
        data = request.get_json()
        brands = data.get('brands', [])
        categorys = data.get('category', '')

        prompt = (
        "Rank the following brands {brands} specifically based on their performance in {category}. "
        "Output the result as a JSON object. Use \"{category}\" as the root key. "
        "Under it, use a \"rank\" key that maps rankings starting from 1, where each rank contains an object "
        "with two keys: \"brand\" and \"reason\". Make sure the rankings reflect current competitive standing."
        )
        
        ai_results = {}
        for category in categorys:
            result = ai_call(prompt, {
                'brands': ', '.join(brands),
                'category': category
            })
            if result is None:
                return {"error": "Failed to get a valid response from the AI model."}, 500  
            else:
                ai_results[category] = result.get(category, {}).get('rank', {})

        if len(ai_results) == len(categorys):
            # Step 2: Create a dummy experiment
            try:
                new_experiment = experiments_table(
                    experiment_name=f"Experiment for {', '.join(brands)} in {', '.join(categorys)}",
                    brands=json.dumps(brands),
                    brand_rank_catagory=json.dumps(categorys),
                    experiment_time=datetime.now()
                )

                db.session.add(new_experiment)
                db.session.commit()
                new_exp_id = new_experiment.id
            except Exception as e:
                return {"error": f"Failed to create experiment: {str(e)}"}, 500
            try:
               for category, rankings in ai_results.items():
                for rank_str, details in rankings.items():
                    result_entry = experiment_results_table(
                        experiment_id=new_exp_id,
                        brand=details['brand'],
                        category=category,
                        rank=float(rank_str),
                        reason=details['reason']
                    )
                    db.session.add(result_entry)
                    db.session.commit()
            except Exception as e:
                return {"error": f"Failed to save results: {str(e)}"}, 500

        return {"message": "Experiment and results saved successfully!",
                "results": ai_results}, 200


            





        
        # print(prompt)
        return brands