from flask import Blueprint, request, jsonify
from App.controllers.job import create_job, get_all_jobs, get_job
from flask_jwt_extended import jwt_required

job_views= Blueprint('job view', __name__)

@job_views.route('/api/create_job', methods=['POST'])
@jwt_required()
def create_job_api():
    data= request.json
    job= create_job(data['title'], data['description'], data['company'])
    return jsonify({'message': 'job was created', 'job_id': job.id}), 201

@job_views.route('/api/view_jobs', methods= ['GET'])
def get_jobs_api():
    jobs= get_all_jobs()
    return jsonify([{'id': job.id, 'title': job.title, 'company': job.company} for job in jobs]), 200