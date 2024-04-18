#!/usr/bin/python3
"""
States view for the API.
"""
from flask import request, jsonify, abort
from models import storage
from models.state import State
from api.v1.views import app_views


@app_views.route('/states/', methods=['GET'], strict_slashes=False)
def get_states():
    """Get all states"""
    all_states = [state.to_dict() for state in storage.all(State).values()]
    return jsonify(all_states)


@app_views.route('/states/<state_id>', methods=['GET'])
def get_state(state_id):
    """Get a specific state by id"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/', methods=['POST'], strict_slashes=False)
def create_state():
    """Create a new state"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    if 'name' not in data:
        return jsonify({"error": "Missing name"}), 400
    state = State(**data)
    state.save()
    return jsonify(state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def update_state(state_id):
    """Update a state"""
    state = storage.get(State, state_id)
    if not state:
        return jsonify({"error": "Not found"}), 404
    if not request.is_json:
        return jsonify({"error": "Not a JSON"}), 400
    data = request.get_json()
    ignore = ['id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict()), 200


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """Delete a state"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200
