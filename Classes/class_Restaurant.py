# Creating a class named Restaurant

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title())
        print(self.cuisine_type.title() + "\n")

    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is open.' + '\n')


restaurant = Restaurant('delightsome chicken', 'average')
restaurant_ = Restaurant('mr biggs', 'fancy')
restaurant__ = Restaurant("domino's", 'middle class')
# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type + "\n")
restaurant.describe_restaurant()
restaurant_.describe_restaurant()
restaurant__.describe_restaurant()
# restaurant.open_restaurant()

