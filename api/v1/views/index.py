from flask import make_response
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
    """Retrieves the number of each objects by type."""
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
