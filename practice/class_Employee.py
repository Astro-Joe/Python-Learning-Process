class Employee():
    
    def __init__(self, firstName, lastName):
        """Initializing attributes..."""
        self.firstName = firstName
        self.lastName = lastName
        self.annualSalary=0

    def give_raise(self, raiseAmount=5000):
        salary = self.annualSalary + raiseAmount
        return salary