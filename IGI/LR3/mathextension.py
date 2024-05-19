def sumOfCubes(arr: list):
    """This function returns a sum of cubes in list"""
    sum = 0.0
    
    for elem in arr:
        sum += pow(elem,3)
    
    return sum

def numbersThatGreater(C: float, arr: list):
    """This function returns a number of numbers in list that are greater than number C"""
    count = 0
    
    for elem in arr:
        if elem > C:
            count += 1
            
    return count

from math import fabs
from math import asin

def arcsin(x:float, eps:float): 
    """This function calcutes arcin for |x| < 1 and returns tuple of x, 
    number of iterations, result, result from math and eps"""
    n = 0
    sum = 0.0
    n2fact = 1
    nfact = 1
    step = eps
    while (n < 500 and fabs(step) >= eps):
        if (n != 0):
            n2fact *= n*2
            nfact *= n

        step = x**(2*n+1)*n2fact/(4**n)/(nfact**2)/(2*n+1)
        sum += step
        n += 1

    return (x, n, sum, asin(x), eps)

def findMaxInList(arr: list):
    """This function finds maximum element in list and returns a tuple, where first element is maximum and second is its index"""
    maximum = arr[0]
    index = 0
    for i in range(len(arr)):
        val = fabs(arr[i])
        if val > maximum:
            maximum = val
            index = i
           
    return (maximum, index)


def productBeforeMaximum(arr: list):
    maximumIndex = findMaxInList(arr)[1]
    
    product = 1
    for i in range(maximumIndex):
        product *= arr[i]
        
    return product