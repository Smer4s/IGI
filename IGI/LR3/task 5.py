from repeated import repeatedTask
from mathextension import *
from input import *

@repeatedTask
def main():
    choice = input("You want to input list by yourself or generate automatically? (1/2)")
    size = inputPosInt("Enter size of list: ")
    if choice == '1':
        floatList = inputList(size)
    else:
        floatList = generateList(size)
        
    C = inputFloat("Enter C:")
    
    print(F"Count of numbers that greater than: {C} is {numbersThatGreater(C, floatList)}")
    print(F"Product of elements before max value: {productBeforeMaximum(floatList)}")
    
    print("List:")
    printList(floatList)

if __name__ == "__main__":
    print(("This program works with a list of float numbers and has this functionality\n"
        "1) Input a list\n"
        "2) Checks for input errors\n"
        "3) Returns count of elements of list, that are greater then number C (C is input number)\n"
        "4) Returns product of elements of list, that located up to the maximum element\n"
        "5) Prints list to screen\n"))
    
    main()
        