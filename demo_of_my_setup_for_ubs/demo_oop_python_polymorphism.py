# Parent Class
class Dog:
    def sound(self):
        return"dog sound"  # Default implementation

# Run-Time Polymorphism: Method Overriding
class Labrador(Dog):
    def sound(self):
        return "Labrador woofs"  # Overriding parent method

class Beagle(Dog): 
    def sound(self):
        return "Beagle Barks"  # Overriding parent method

# Compile-Time Polymorphism: Method Overloading Mimic
class Calculator:
    """
    This is a class that calculates a sum of 3 or less numbers.
    """
    def add(self, a, b=0, c=0):
        return a + b + c  # Supports multiple ways to call add()

# Run-Time Polymorphism
def runDemo():
    dog1 = Dog()
    lab1 = Labrador()
    beagle1 = Beagle()
    dog1_sound = dog1.sound()
    lab1_sound = lab1.sound()
    beagle1_sound = beagle1.sound()
    print(f"The initial sound that the dog makes is: {dog1_sound}")
    print(f"The new sound that the labrador makes is {lab1_sound}")
    print(f"The new sound that the beagle makes is {beagle1_sound}")
    
    # Compile-Time Polymorphism (Mimicked using default arguments)
    calc = Calculator()
    print(f"When there are only two arguments of 5 and 10, the answer is the sum which is {calc.add(5, 10)}")  # Two arguments
    print(f"When there are three arguments of 5, 10 and 15, the answer is the sum of all three which is  {calc.add(5, 10,15)}")  # Three arguments

if __name__ == "__main__":
    runDemo()