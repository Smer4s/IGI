# LR 3, Task 2, Studenichnik Nikita Igorevich 253503.
# This program creates a cycle of ints and adds cube of every int.
# 24.03.2024

from repeated import repeatedTask
from input import inputListWhile
from mathextension import sumOfCubes

@repeatedTask
def main():
    arr = inputListWhile()
    print (f"Sum of cubes is: {sumOfCubes(arr)}")

if __name__ == "__main__":
    print('This program creates a cycle of ints and adds cube of every int. To end input enter number: 12')  
    main()
        
        