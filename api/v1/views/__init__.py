#!/usr/bin/python3
"""
Package for API views.
"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import all modules to avoid circular imports
from api.v1.views.index import *
