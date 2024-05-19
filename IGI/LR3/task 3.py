from repeated import repeatedTask

from stringextension import isBinaryNumber

@repeatedTask
def main():
    string = input("Enter a string to determine: ")
    if isBinaryNumber(string):
        print("This string is binary number")
    else:
        print("This string is not binary number")

if __name__ == "__main__":
    main()