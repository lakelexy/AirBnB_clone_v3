#!/usr/bin/python3

"""index file for flask app"""

from api.v1.views import app_views
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
from flask import jsonify

@app_views.route('/status', strict_slashes=False)
def api_status():
    """a function to return api status"""
    
    return jsonify({"status": "OK"})

@app_views.route('/stats', strict_slashes=False)
def obj_stats():
    """returns the number of each object"""

    my_dict = {
            "amenities": storage.count(Amenity), 
            "cities": storage.count(City),
            "places": storage.count(Place),
            "reviews": storage.count(Review),
            "states": storage.count(State),
            "users": storage.count(User)
            }
    return jsonify(my_dict)
