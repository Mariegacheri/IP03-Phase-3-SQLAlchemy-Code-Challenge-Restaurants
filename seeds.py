from sqlalchemy.orm import sessionmaker
from models import Customer, Restaurant, Review

def seed_data(session):
    # Creating some sample data
    customer1 = Customer(first_name='Tyler', last_name='Smart')
    customer2 = Customer(first_name='Cte', last_name='Waina')

    restaurant1 = Restaurant(name='Steakhouse', price=3)
    restaurant2 = Restaurant(name='Tatu Restuarant', price=2)

    review1 = Review(restaurant=restaurant1, customer=customer1, star_rating=4)
    review2 = Review(restaurant=restaurant1, customer=customer2, star_rating=5)
    review3 = Review(restaurant=restaurant2, customer=customer1, star_rating=3)

    # Add data to the session and commit
    session.add_all([customer1, customer2, restaurant1, restaurant2, review1, review2, review3])
    session.commit()

    print("Sample data added to the database.")

# Database URL
DATABASE_URL = 'sqlite:///Restuarants.db' 

# Creating the database engine
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Seeding the database with sample data
seed_data(session)