class Dog:
    def __init__(self, name, breed, age):
        self.name = name  # Public attribute
        self._breed = breed  # Protected attribute
        self.__age = age  # Private attribute
        #The more underscores you put, the more protected the attribute is 

    # Public method
    def getInfo(self):
        """
        Gets info about the dog
        """
        return f"Name: {self.name}, Breed: {self._breed}, Age: {self.__age}"

    # Getter and Setter for private attribute
    # def getAge(self):
    #     """
    #     Gets the age of the dog
    #     """
    #     return self.__age

    # def setAge(self, age):
    #     """
    #     Allows an age to be set to the dog
    #     """
    #     if age > 0:
    #         self.__age = age
    #     else:
    #         print("Invalid age!")

    @property
    def age(self):
        """
        Gets the age of the dog
        """
        return self.__age
    
    @age.setter
    def age(self,value):
        """
        Allows an age to be set to the dog
        """
        if value > 0:
            self.__age = value
        else:
            print("Invalid age!")

        
        

def runDemo():
    """
    Runs the demo
    """
    # Example Usage
    dog = Dog("Buddy", "Labrador", 3)

    # Accessing public member
    print(dog.name)  # Accessible

    # Accessing protected member
    print(dog._breed)  # Accessible but discouraged outside the class

    # Accessing private member using getter
    print(dog.age)

    # Modifying private member using setter
    dog.age = 5
    print("The age of the dog has been modified to 5")
    print(dog.getInfo())


if __name__ == "__main__":
    runDemo()