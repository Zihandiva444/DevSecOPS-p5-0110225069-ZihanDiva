from flask import Blueprint, jsonify, request
from .models import TaskStore
from .validators import validate_title

bp = Blueprint("tasks", __name__)
store = TaskStore()


@bp.get("/tasks")
def list_tasks():
    return jsonify(store.all())


@bp.post("/tasks")
def create_task():
    data = request.get_json(silent=True) or {}
    ok, result = validate_title(data.get("title"))
    if not ok:
        return jsonify({"error": result}), 400
    return jsonify(store.add(result).to_dict()), 201


@bp.put("/tasks/<int:task_id>/done")
def mark_done(task_id):
    task = store.get(task_id)
    if task is None:
        return jsonify({"error": "Task tidak ditemukan"}), 404
    task.done = True
    return jsonify(task.to_dict())


@bp.delete("/tasks/<int:task_id>")
def delete_task(task_id):
    if not store.delete(task_id):
        return jsonify({"error": "Task tidak ditemukan"}), 404
    return "", 204