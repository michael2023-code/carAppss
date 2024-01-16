from app import db

class Sales(db.Model):
    __tablename__ = "sales"    
    sale_id = db.Column(db.Integer, primary_key = True)
    payment_method = db.Column(db.String)
    amount = db.Column(db.Integer)
    status = db.Column(db.String(100))
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def serialize(self):
        return(
            {
                "sale_id" : self.sale_id,
                "payment_method" : self.payment_method,
                "amount" : self.amount,
                "status" : self.status,
                "car_id" : self.car_id,
                "user_id" : self.user_id,
                "car_details" : self.car.serialize() if self.car else None,
                "user_details" : self.user.serialize() if self.user else None          
            }
        )