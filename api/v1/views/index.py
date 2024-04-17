#!/usr/bin/python3
"""
API view that handles all default RESTful API actions for
stats in AirBnB clone v3.
"""

from flask import jsonify, make_response
import json
from models import storage
from api.v1.views import app_views
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


@app_views.route('/stats', methods=['GET'])
def stats():
    """
    Retrieves the number of each type of object by type.
    Returns:
        - JSON response with the object count for each type.
    """
    stats = {
        "users": storage.count(User),
        "states": storage.count(State),
        "cities": storage.count(City),
        "amenities": storage.count(Amenity),
        "places": storage.count(Place),
        "reviews": storage.count(Review)
    }
    response = make_response(json.dumps(stats, indent=2, sort_keys=False))
    response.mimetype = 'application/json'
    return response
