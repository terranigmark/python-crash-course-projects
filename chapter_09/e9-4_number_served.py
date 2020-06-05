
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant {self.restaurant_name} specializes in {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

    def set_number_served(self, customers):
        self.number_served = customers

    def increment_number_served(self, customers):
        self.number_served += customers

restaurant = Restaurant('La gran esquina de los chorizos', 'Colombian')

#restaurant.number_served = 5
restaurant.set_number_served(10)
restaurant.increment_number_served(3)
print(restaurant.number_served)