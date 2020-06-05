
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant {self.restaurant_name} specializes in {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

restaurant = Restaurant('La gran esquina de los chorizos', 'Colombian')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()