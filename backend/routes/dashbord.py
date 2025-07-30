from flask import Flask
import json
import requests
from flask_cors import cross_origin
from database.model import *
from flask import request


def dashbord_cards(app):
    @app.route('/api/dashbord-card', methods=['GET'])
    @cross_origin(origin='http://localhost:8080')
    def dashbord_cards():
        experiments = experiments_table.query.order_by(experiments_table.experiment_time.desc()).all()
        exp_data = {}

        for experiment in experiments:
            exp_data[experiment.id] = {
                'experiment_name': experiment.experiment_name,
                'brands': json.loads(experiment.brands),
                'categorys': json.loads(experiment.brand_rank_catagory),
                'experiment_time': experiment.experiment_time.strftime('%Y-%m-%d %H:%M:%S'),
                'results': {},
                'avg_rank': {}
            }

            for result in experiment.results:
                brand = result.brand
                category = result.category
                rank = result.rank

                if brand not in exp_data[experiment.id]['results']:
                    exp_data[experiment.id]['results'][brand] = {}
                exp_data[experiment.id]['results'][brand][category] = rank

            # Now calculate average ranks
            for brand, cat_ranks in exp_data[experiment.id]['results'].items():
                rank_values = list(cat_ranks.values())
                avg_rank = sum(rank_values) / len(rank_values)
                exp_data[experiment.id]['avg_rank'][brand] = round(avg_rank, 2)
        print(exp_data)

        return exp_data
