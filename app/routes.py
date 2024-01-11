from flask import Blueprint
from app.controllers.user_controller import create_user, get_users
from app.controllers.car_controller import create_car, get_cars

bp = Blueprint('bp', __name__)

@bp.route('/users', methods=['POST'])
def add_user():
    return create_user()

@bp.route('/users', methods=['GET'])
def list_users():
    return get_users()

@bp.route('/cars', methods=['POST'])
def add_car():
    return create_car()

@bp.route('/cars', methods=['GET'])
def list_cars():
    return get_cars()