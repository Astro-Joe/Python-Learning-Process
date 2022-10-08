class User():
    def __init__(self, first_name, last_name, location, usr_name, login_attempts):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.location = location.title()
        self.usr_name = usr_name.title()
        self.login_attempts = login_attempts


    def describe_user(self):
        full_name = self.first_name + ' ' + self.last_name
        print("Your name is", full_name)
        print("Your username is " + self.usr_name)
        print("You are at", self.location)

    def greet_user(self):
        full_name = self.first_name + ' ' + self.last_name
        print("\nHello", full_name + '!.')

    # def increment_login_attempts(self):
    #     attempt = [0,1]
    #     item = 1
    #     if item > 0:
    #         item+=1
    #         attempt[0] = item
    #         self.login_attempts = attempt[0]
 

    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges():
    def __init__(self, *privileges):
        self.privileges = list(privileges)
    


    def show_privileges(self):
            print("These are the list of Admin privileges: ")
            for privilege in self.privileges:
                print("\t-" + str(privilege.title()))


class Admin(Privileges):
    def __init__(self, *user):
        self.user = user
        super().__init__('privileges')
        self.user = list(self.privileges)
        self.privileges = Privileges()
    

    





user = Admin('can add post', 'can ban user', 'can delete post')
# user.describe_user()
# user.greet_user()
# user.increment_login_attempts()
# print(user.login_attempts)
# user.reset_login_attempts()
# print(user.login_attempts)
user.privileges.show_privileges()
