# LR 3, Task 1, Studenichnik Nikita Igorevich 253503.
# This program calculates arcsin(x) for epsilon
# 24.03.2024

from math import fabs

from repeated import repeatedTask
from input import inputFloat
from mathextension import arcsin

@repeatedTask
def main():
    x = inputFloat("Enter x: ")
    while fabs(x) >= 1:
        print("|x| must be less than 1, try again")
        x = inputFloat()
                  
    eps = inputFloat("Enter epsilon: ")
            
    result = " | ".join([item.__str__() for item in arcsin(x,eps)])
        
    print("| x | n | F(x) | Math F(x) | eps |")
    print("|", result, "|")

if __name__ == "__main__":
    print("This program calculates arcsin(x) with accuracy epsilon")
    main()