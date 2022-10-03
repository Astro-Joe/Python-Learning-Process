# Creating a class named Restaurant

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name.title())
        print(self.cuisine_type.title() + "\n")

    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is open.' + '\n')


    def  number_peeps(self):
         print(str(self.number_served) + " people have been served in " + self.restaurant_name)
    
    def set_number_served(self, number):
        self.number_served = number   


    def increament_number_served(self, number):
        self.number_served += number


# restaurant = Restaurant('delightsome chicken', 'average')
# restaurant_ = Restaurant('mr biggs', 'fancy')
# restaurant__ = Restaurant("domino's", 'middle class')
# # print(restaurant.restaurant_name)
# # print(restaurant.cuisine_type + "\n")
# restaurant.describe_restaurant()
# restaurant_.describe_restaurant()
# restaurant__.describe_restaurant()
# restaurant.open_restaurant()
description = Restaurant("Mr biggs", "Fancy")
# description.number_served = 11
description.set_number_served(11)
description.number_peeps()
