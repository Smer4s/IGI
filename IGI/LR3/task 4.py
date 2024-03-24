# LR 3, Task 4, Studenichnik Nikita Igorevich 253503.
# This program analyzes text and 
# 1) return number of lowercase letters
# 2) returns last word that contains letter 'i' and its index
# 3) returns string without words that begins with 'i'
# 24.03.2024

from stringextension import *

if __name__ == "__main__":
    string = ("So she was considering in her own mind, "
    "as well as she could, for the hot day made her "
    "feel very sleepy and stupid, whether the pleasure "
    "of making a daisy-chain would be worth the trouble "
    "of getting up and picking the daisies, when suddenly "
    "a White Rabbit with pink eyes ran close by her.")
    
    print(f"Number of lowercase letters is: {lowercaseLettersCount(string)}")
    
    word = findWord(string)
    if word != None:
        print(f"Word, that begins with 'i' is: '{word[0]}' and its index is: {word[1]}")
    else:
        print("There is no words, that begins with 'i'")
        
    print("Text without words, that begins with 'i': ")
    print(excludeWords(string))