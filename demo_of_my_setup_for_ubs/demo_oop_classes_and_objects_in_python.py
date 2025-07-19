

class Dog:
    """
    This is a class for a dog

    """
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        # init is the name of the constructor
        """
        Constructor of th dog class
        :param name: name of dog
        :param age: age of dog

        """
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

def runDemo():
    """
    Runs the demo
    """
    my_dog = Dog("Bingo",5)
    #my_dog: Dog = Dog(name="Bing", age=5)
    #The above commented method is better to be sure of what you are passing
    print(f"The dogs name is {my_dog.name}. His age is {my_dog.age}. It is of species {my_dog.species}")
    Dog.species = "Feline"

    print(f"The species of the dog has been modified to {my_dog.species}")  # (Updated class variable)
   
if __name__ == "__main__":
    runDemo()