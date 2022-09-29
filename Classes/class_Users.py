class User():
    def __init__(self, first_name, last_name, location, usr_name):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.location = location.title()
        self.usr_name = usr_name.title()

    def describe_user(self):
        full_name = self.first_name + ' ' + self.last_name
        print("Your name is", full_name)
        print("Your username is " + self.usr_name)
        print("You are at", self.location)

    def greet_user(self):
        full_name = self.first_name + ' ' + self.last_name
        print("\nHello", full_name + '!.')


user = User('joseph', 'ilemobayo', 'ikorodu', 'astrojoe')
user.describe_user()
user.greet_user()
