
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant {self.restaurant_name} specializes in {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")


tijuana = Restaurant('Tijuana', 'mexican')
pizza_mole = Restaurant('Pizza Mole', 'italian')
chef_burger = Restaurant('Chef Burger', 'american')

tijuana.describe_restaurant()
pizza_mole.describe_restaurant()
chef_burger.describe_restaurant()