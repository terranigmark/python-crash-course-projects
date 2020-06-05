
class Restaurant:

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

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['maracuya', 'berries', 'hazelnut', 'bubble gum', 'pistaccio']

    def show_menu(self):
        print("We have the following flavors:")
        for flavor in self.flavors:
            print(f"\t{flavor.title()}")

restaurant = Restaurant('La gran esquina de los chorizos', 'Colombian')

baskin_robbins = IceCreamStand('Baskin Robbins', 'Ice Creams')
print(baskin_robbins.restaurant_name)
baskin_robbins.show_menu()