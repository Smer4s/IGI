def isBinaryNumber(string: str):
    """This function if an inputed string is a binary number(like 1001001010)"""
    for symbol in string:
        if (symbol != '1') == (symbol != '0'):
            return False
    
    return True

def lowercaseLettersCount(string: str):
    """This function returns count of lowercase letters in string"""
    count = 0
    for symbol in string:
        if symbol.isalpha() and symbol.lower() == symbol:
            count += 1
            
    return count

def parseTextToWords(text: str):
    """This function return a text as a list of words separated by " ,." symbols"""
    return ''.join([i for i in text]).split(' ')

def findWord(text: str):
    """This function finds a word in a text that begin with 'i' and return that word with its index"""
    words = parseTextToWords(text)
    for i in range(len(words)- 1, 0, -1):
        if words[i][0].lower() == 'i':
            return (words[i], i + 1)
        
def excludeWords(text: str):
    """This function deletes all words from text that begins with 'i'"""
    arr = []
    words = parseTextToWords(text)
    
    for symbol in words:
        if symbol[0].lower() != 'i':
            arr.append(symbol)
    
    return ' '.join(arr)