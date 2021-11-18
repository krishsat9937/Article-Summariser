from flask import Blueprint
from .views import process_summary

# set method as endpoint

# Create the blueprint for this app
api = Blueprint('api', __name__, url_prefix='/api')

# Add the view as route; methods like GET, POST, PUT will automatically route to class methods with parameters
api.add_url_rule('get_summary/', view_func=process_summary, methods=['POST'])