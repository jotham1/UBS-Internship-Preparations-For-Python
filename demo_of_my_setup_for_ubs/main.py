import matplotlib.pyplot as plt
import numpy as np

def myDetails(name :str,age : int,school : str):
        """
        Function used to display details about the user
        param name: is the first argument
        param age: is the second argument
        param school: is the third argument
        return: No returned value
        """
        print(f"My name is {name}")
        print(f"I am {age} years old")
        print(f"I go to a school named {school} ")

def simpleMatplotlibDemo():
        """
        Function used to display a simple graph
        return: No returned value
        """
        fig, ax = plt.subplots()             # Create a figure containing a single Axes.
        ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
        plt.show()                           # Show the figure.

def argandDiagram():
       """
       """
       
       
          

if __name__ == "__main__":
    myDetails(name="Jotham Akinremi", age=17, school="Super Herors High School")
    simpleMatplotlibDemo()
    