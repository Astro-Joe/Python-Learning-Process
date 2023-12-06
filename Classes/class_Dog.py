class Dog():
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
        
    def sit(self):
        """Simulates a dog sitting down in response to a command."""
        print(self.name.title() + ' is now sitting.')
        