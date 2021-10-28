from flask import Blueprint, jsonify, make_response, request, abort
from flask.helpers import make_response
from flask.json import tojson_filter
from werkzeug.utils import header_property
from app.models.task import Task
from app import db

task_bp = Blueprint("task", __name__,url_prefix ="/tasks")

# Helper Functions
# TODO:PUT ANY HELPER FUNCTIONS header_property

# Routes
@task_bp.route("", methods=["POST"])
def create_task():
    request_body = request.get_json()
    if "title" not in request_body or "description" not in request_body:
        return make_response({"details": "Invalid data"}, 400)

    new_task = Task(
        title=request_body["title"],
        description=request_body["description"]
    )

    db.session.add(new_task)
    db.session.commit()

    return make_response(new_task.to_dict(), 201)

@task_bp.route("", methods=["GET"])
def read_all_tasks():
    tasks = Task.query.all()

    task_response = []
    for task in tasks:
        task_response.append(
            task.to_dict()
        )
    return make_response(jsonify(task_response), 200)
