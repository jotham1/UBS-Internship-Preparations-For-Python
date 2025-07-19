# Single Inheritance
class Dog:
    def __init__(self, name):
        self.name = name

    def displayName(self):
        """
        Method to display the name of the dog
        """
        print(f"Dog's Name: {self.name}")

class Labrador(Dog):  # Single Inheritance(Labrador inherits methods and characteristics from dog class)
    def sound(self):
        """
        Method to display the sound the dgo makes
        """
        print("Labrador woofs")

# Multilevel Inheritance
class GuideDog(Labrador):  # Multilevel Inheritance(Guide dog inherits from labrador but also inherits from dog )
    def guide(self):
        """
        Method to show the job of a guide dog
        """
        print(f"{self.name}Guides the way!")

# Multiple Inheritance
class Friendly:
    def greet(self):
        """
        Method to display the dogs nature
        """
        print("Friendly!")

class GoldenRetriever(Dog, Friendly):  # Multiple Inheritance(Golden retrever inherits from both dog and friendly even though they are unrelated)
    def sound(self):
        print("Golden Retriever Barks")
def runDemo():
    """
    Runs the demo
    """
    # Example Usage
    lab = Labrador("Buddy")
    lab.displayName()
    lab.sound()

    guide_dog = GuideDog("Max")
    guide_dog.displayName()
    guide_dog.guide()

    retriever = GoldenRetriever("Charlie")
    retriever.displayName()
    retriever.greet()
    retriever.sound()

if __name__ == "__main__":
    runDemo()