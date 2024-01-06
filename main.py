# Imporing the classes
from customer import Customer
from restaurant import Restaurant
from review import Review

# Creating the engine and the session
engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

# Our example code
customer1 = Customer("Tyler", "Smart")
customer2 = Customer("Cate", "Waina")

restaurant1 = Restaurant("Steakhouse")
restaurant2 = Restaurant("Tatu Restaurant")

review1 = customer1.add_review(restaurant1, 4)
review2 = customer2.add_review(restaurant1, 5)
review3 = customer1.add_review(restaurant2, 3)

# Access information
print(customer1.full_name())  
print(restaurant1.average_star_rating())  
print(Customer.find_by_name("Tyler Smart")) 
print(Customer.find_all_by_given_name("Tyler"))