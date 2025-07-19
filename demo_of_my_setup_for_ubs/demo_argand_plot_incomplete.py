import matplotlib.pyplot as plt
import numpy as np  
from typing import List, Any
import random 

def createComplexNumbers(n: int) -> List[Any]:
    """
    purpose of function is to return a list of complex numbers
    param n: number of complex numbers to be returned
    return my_list: returns a list of complex numbers 
    """
    
    complex_numbers = []
    for i in range(n):  
        real = random.randint(1,10)
        imaginary = random.randint(1,10) 
        complex_numbers.append(real + imaginary*1j)
        
    return complex_numbers
        



def plotArgand():  # Create a complex number
    z = [complex(s) for s in createComplexNumbers(10)]

    # Create a figure and axis
    fig, ax = plt.subplots()

    for i in range(10):
        # Plot the real and imaginary parts
        ax.plot([0, z[i].real], [0, z[i].imag], marker='o', color='blue')

        # Set labels and title
        ax.set_xlabel('Real Part')
        ax.set_ylabel('Imaginary Part')
        ax.set_title('Argand Diagram')

        # Set equal scaling
        ax.axis('equal')

        # Show grid
        ax.grid(True)

    # Show the plot
    plt.show()

# Create polar plot of a number of complex numbers
def plotPolar():
    # Create a list of complex numbers
    # add you code here..
    # ..
    # ..
    
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    #ax.scatter(angles, magnitudes, color='red')
    ax.set_title('Polar Plot of Complex Numbers')
    plt.show()




if __name__ == "__main__":
    plotArgand()
    plotPolar()