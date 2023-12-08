class User():
    def __init__(self, first_name, last_name, location, usr_name):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.location = location.title()
        self.usr_name = usr_name.title()
        self.login_attempts = [0]


    def describe_user(self):
        full_name = self.first_name + ' ' + self.last_name
        print("Your name is", full_name)
        print("Your username is " + self.usr_name)
        print("You are at", self.location)

    def greet_user(self):
        full_name = self.first_name + ' ' + self.last_name
        print("\nHello", full_name + '!.')

    def increment_login_attempts(self):
        flag = True 
        while flag:
            increment = self.login_attempts + 1
            self.login_attempts = increment
            flag = False
        print('There have been ' + str(increment) + ' login attempts')
        
    def reset_login_attempts(self, attempt):
        self.login_attempts[0] = 0


class Admin(User):
    """Initializing attributes of Admin"""
    def __init__(self, first_name, last_name, location, usr_name):
        """Initializing attributes of superclass"""
        super().__init__(first_name, last_name, location, usr_name)
        self.priviledges = ['can add post', 'can delete post', 'can ban user']
    
    
    
    

    





