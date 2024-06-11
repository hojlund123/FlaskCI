from flask import request, jsonify
from utils.job import add_job

def configure_routes(app):
    @app.route('/add-job', methods=['POST'])
    def add_job_route():
        data = request.json
        add_job(data)
        return jsonify({'status': 'Job added'}), 200
