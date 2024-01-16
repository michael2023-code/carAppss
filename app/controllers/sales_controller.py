from flask import request, jsonify
from app import db
from app.models.sales_model import Sales
from sqlalchemy.exc import SQLAlchemyError
import logging

logging.basicConfig(level=logging.INFO)


def handle_error(e, status_code):
    logging.error(str(e))
    return jsonify({'error': str(e)}), status_code

# (/sales) C
def create_sale():
    try:
        data = request.get_json()

        if 'payment_method' not in data or 'amount' not in data or 'status' not in data:
            return handle_error('Missing data fields (payment_method, amount, status required)', 400)

        new_sale = Sales(payment_method=data['payment_method'], amount=data['amount'], status=data['status'])
        db.session.add(new_sale)
        db.session.commit()
        logging.info(jsonify(new_sale.serialize()))
        return jsonify(new_sale.serialize()), 201

    except SQLAlchemyError as e:
        return handle_error(e, 500)
    

# (/sales) R
def get_sales():
    try:
        sales = Sales.query.all()
        return jsonify([sale.serialize() for sale in sales]), 200
    except SQLAlchemyError as e:
        return handle_error(2, 500)
    
    
# (/sales/sale_id)
def get_sale(sale_id):
    try:
        sale = Sales.query.filter_by(id = sale_id).first()
        return jsonify(sale.serialize())
    except SQLAlchemyError as e:
        return handle_error(e, 500)


# (/sales/sale_id) U
def update_sale(sale_id):
    try:
        sale = Sales.query.filter_by(id = sale_id).first()
        data = request.get_json()
        for attr in data:
            setattr(sale, attr, data[attr])
        
        db.session.commit()
        
        return jsonify(sale.serialize()), 200
    
    except SQLAlchemyError as e:
        return handle_error(e, 500)
    
# (/sales/sale_id) D
def delete_sale(sale_id):
    try:
        sale = Sales.query.filter_by(id = sale_id).first()
        
        db.session.delete(sale)
        db.session.commit()
        
        return jsonify({"Message": "Deleted Successesfully"})
    
    except SQLAlchemyError as e:
        return handle_error(e, 500)