#!/usr/bin/python3
"""
Module for index view.
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def api_status():
    """
    Return the status of the API.
    """
    return jsonify({"status": "OK"})
