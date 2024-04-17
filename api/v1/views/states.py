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
    if not request.json:
        abort(400, description="Not a JSON")
    if 'name' not in request.json:
        abort(400, description="Missing name")
    state = State(**request.get_json())
    state.save()
    return jsonify(state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def update_state(state_id):
    """Update a state"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    if not request.json:
        abort(400, description="Not a JSON")
    ignore = ['id', 'created_at', 'updated_at']
    for key, value in request.get_json().items():
        if key not in ignore:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """Delete a state"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200
