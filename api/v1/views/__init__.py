# api/v1/views/__init__.py
from flask import Blueprint

app_views = Blueprint('app_views', __name__)

# Wildcard import to avoid circular import errors
from api.v1.views.index import *
