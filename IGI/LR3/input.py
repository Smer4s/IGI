def inputFloat(string: str = "Enter a number: "):
    """This function inputs a float number until it sucessfuly inputed"""
    while True:
        try:
            C = float(input(string))
            return C
        except ValueError:
            print("This number is not a float number, try again")
            
def inputInt(string: str = "Enter a number: "):
    """This function inputs an int number until it sucessfuly inputed"""
    while True:
        try:
            C = int(input(string))
            return C
        except ValueError:
            print("This number is not an integer number, try again")
                      
def inputPosInt(string: str = "Enter a number: "):
    """This function inputs a positive int number until it sucessfuly inputed"""
    while True:
        C = inputInt(string)
        if C > 0:
            return C
        print("Number must be positive integer value")
            
def inputList(size: int):
    """This function returns a list of float numbers that are inputed by user"""
    arr = []
    for i in range(size):
        num = inputFloat(f"Enter arr[{i}]: ")
        arr.append(num)
        
    return arr

def printList(arr: list):
    """This function prints every single element in a list"""
    for i in arr:
        print(i)

def inputListWhile(delimeter: int = 12):
    """This function generates input elements until a delimeter is provided"""
    return iter(lambda: inputFloat(), delimeter)    
    
import random

def generateList(size: int):
    """This function generates a list of float numbers"""
    return [random.uniform(-100.0,100.0) for _ in range(size)]
 
       
    
 