# seeds.py
from models import Restaurant, Customer, Review, db

# Create sample data
sample_restaurant1 = Restaurant(name="SteakHouse", price=3)
sample_restaurant2 = Restaurant(name="  Tatu Restaurant", price=2)

sample_customer1 = Customer(first_name="Kylan", last_name="Gatia")
sample_customer2 = Customer(first_name="Cate", last_name="Fatma")

db.session.add_all([sample_restaurant1, sample_restaurant2, sample_customer1, sample_customer2])
db.session.commit()

# Add reviews
review1 = Review(restaurant=sample_restaurant1, customer=sample_customer1, star_rating=4)
review2 = Review(restaurant=sample_restaurant2, customer=sample_customer1, star_rating=5)
review3 = Review(restaurant=sample_restaurant1, customer=sample_customer2, star_rating=3)

db.session.add_all([review1, review2, review3])
db.session.commit()
