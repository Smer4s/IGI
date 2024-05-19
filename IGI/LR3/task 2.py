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
        
        