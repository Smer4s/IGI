# LR 3, Task 3, Studenichnik Nikita Igorevich 253503.
# This program determines if an inputed string is a binary number(like 1001001010)
# 24.03.2024

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