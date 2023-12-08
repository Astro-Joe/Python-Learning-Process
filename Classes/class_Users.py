class User():
    def __init__(self, first_name, last_name, location, usr_name):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.location = location.title()
        self.usr_name = usr_name.title()
        self.login_attempts = [0]


    def describe_user(self):
        full_name = self.first_name + ' ' + self.last_name
        print("Full name:", full_name)
        print("Username:", self.usr_name)
        print("Location:", self.location)

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
        pass


class Admin(User):
    """Modelling an Administrator"""
    def __init__(self, first_name, last_name, location, usr_name):
        """Initializing attributes of Admin"""
        super().__init__(first_name, last_name, location, usr_name)
        """Initializing attributes of superclass"""
        self.privileges = ['can add post', 'can delete post', 'can ban user']
        
    
    def show_priviledges(self):
        """Shows the priviledges of said admin"""
        # print(self.first_name + ' has the following privileges')     
        for privilege in self.privileges:
            print('\t-' + privilege.title())
                   

    

user = Admin('joseph', 'ilemoabyo', 'lagos', 'the_boss')
print(user.describe_user())
print(user.first_name + ' has the following privileges')  
user.show_priviledges()




