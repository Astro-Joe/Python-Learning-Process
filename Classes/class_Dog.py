class Dog(object): # Format for python 2.7
    """A simple attempt to model a dog."""
    
    # Initializing the attributes of the Class.
    # The 'self' parameter is compulsory when initializing attributes of a class.
    def __init__(self, name, age): #The parameters are called attributes of the class.
        """Initialize name and age attributes."""
        self.name = name # Makes the variable accessible to evry method in the class an instances created from the class.
        self.age = age
    
    # A function that is part of a class is called a method.  
    def sit(self):
        """Simulates a dog sitting down in response to a command."""
        print(self.name.title() + ' is now sitting.')
        
    def roll_over(self):
        """Simulates rolling over in response to a command."""
        print(self.name.title() + ' rolled over!')
        
        
my_dog = Dog('willie', 6) # Creating an instance with having the attributes of the class_Dog

# Calling methods
my_dog.sit()
my_dog.roll_over()

# print("My dog's name is "  + my_dog.name.title() + ".")
# print("My dog is " + str(my_dog.age) + " years old.")

#print(my_dog.name) # Prints the argument assigned to the attribute 'name' in the instance created.
#print(my_dog.age) # Prints the argument assigned to the attribute 'age' in the instance created.