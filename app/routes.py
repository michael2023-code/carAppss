from flask import request, Blueprint
from app.controllers.user_controller import create_user, get_users, patch_user, delete_user
from app.controllers.car_controller import create_car, get_cars 
from app.controllers.sales_controller import create_sale, get_sales, get_sale, delete_sale, update_sale

bp = Blueprint('bp', __name__)

# home(/)
@bp.route('/')
def home():
    return '<h1>User API</h1>'

@bp.route('/users', methods=['POST', 'GET'])
def users():
    if request.method == "GET": 
         return get_users()
    elif request.method == "POST":
         return create_user()

@bp.route('/users/<int:id>', methods=['PATCH', 'DELETE'])
def user(id):
    if request.method == "PATCH": 
         return patch_user(id)
    elif request.method == "DELETE":
         return delete_user(id)


@bp.route('/cars', methods=['POST'])
def add_car():
    return create_car()
 
@bp.route('/cars', methods=['GET'])
def list_cars():
    return get_cars()

""" CARS """
# (/cars) C
@bp.route('/cars', methods=['POST'])
def add_car():
    if request.method=="POST":
        return create_car()

# # (/cars) R
@bp.route('/cars', methods=['GET'])
def list_cars():
    return get_cars()

# (/cars/car_id) R
@bp.route('/cars/<int:car_id>', methods = ['GET'])
def read_car(car_id):
    return(get_car(car_id))


# (/cars/car_id) U
@bp.route('/cars/<int:car_id>', methods = ["PATCH"])
def patch_car(car_id):
    if request.method=="PATCH":
        return(update_car(car_id))

# (/cars/car_id) D
@bp.route('/cars/<int:car_id>', methods = ['DELETE'])
def remove_car(car_id):
    if request.method=="DELETE":
        return(delete_car(car_id))


""" SALES """
# (/sales) C
@bp.route('/sales', methods=['POST'])
def add_sale():
    if request.method=="POST":
        return create_sale()

# (/cars) R
@bp.route('/sales', methods=['GET'])
def list_sales():
    return(get_sales())

# (/sales/sale_id) R
@bp.route('/sales/<int:sale_id>', methods = ['GET'])
def read_sale(sale_id):
    return(get_sale(sale_id))

# (/sales/sales_id) U
@bp.route('/sales/<int:sale_id>', methods = ["PATCH"])
def patch_sale(sale_id):
    if request.method=="PATCH":
        return(update_sale(sale_id))

# (/cars/car_id) D
@bp.route('/sales/<int:sale_id>', methods = ['DELETE'])
def remove_sale(sale_id):
    if request.method=="DELETE":
        return(delete_sale(sale_id))