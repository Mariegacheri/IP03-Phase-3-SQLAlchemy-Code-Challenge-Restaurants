# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    star_rating = db.Column(db.Integer)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    restaurant = db.relationship('Restaurant', back_populates='reviews')
    customer = db.relationship('Customer', back_populates='reviews')

class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)
    reviews = db.relationship('Review', back_populates='restaurant')

    @classmethod
    def fanciest(cls):
        return cls.query.order_by(cls.price.desc()).first()

    def all_reviews(self):
        return [review.full_review() for review in self.reviews]

class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    reviews = db.relationship('Review', back_populates='customer')

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def favorite_restaurant(self):
        return max(self.reviews, key=lambda r: r.star_rating).restaurant

    def add_review(self, restaurant, rating):
        new_review = Review(restaurant=restaurant, customer=self, star_rating=rating)
        db.session.add(new_review)
        db.session.commit()

    def delete_reviews(self, restaurant):
        reviews_to_delete = [review for review in self.reviews if review.restaurant == restaurant]
        for review in reviews_to_delete:
            db.session.delete(review)
        db.session.commit()

# Add this to the end of the file
db.create_all()
