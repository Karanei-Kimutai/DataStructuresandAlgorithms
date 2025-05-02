from functools import lru_cache

def fibonacci(nthnumberofthesequence:int):
    if nthnumberofthesequence==1:
        return 0
    elif nthnumberofthesequence==2:
        return 1
    else:
        return fibonacci(nthnumberofthesequence-1)+fibonacci(nthnumberofthesequence-2)

for i in range(1,11):
  print(fibonacci(i),end=" ")


fibonacciCache={}#A dictionary that stores the key value pairs-> nthfibonaccinumber:value
def fibonacciversion2(n:int):
    if n in fibonacciCache:
        return fibonacciCache[n]  #Basically,...if key in cache, return the value
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        value=fibonacciversion2(n-1)+fibonacciversion2(n-2)
    fibonacciCache[n]=value  #stores results of previously computed fibonacci numbers thus avoiding redundant calculations
    return value

for i in range(10):
    print(f"{i}:{fibonacciversion2(i)}")

@lru_cache(maxsize=100)   #Used to cache(store) results of previously computed fibonacci numbers to avoid redundant calculations
def fibonacciversion3(nthnumberofthesequence:int):
    if nthnumberofthesequence==1:
        return 0
    elif nthnumberofthesequence==2:
        return 1
    else:
        return fibonacciversion3(nthnumberofthesequence-1)+fibonacciversion3(nthnumberofthesequence-2)

for i in range(10):
    fibonacciversion3(i)

#Finding the sum of a list using recursion
def sumOfList(listOfNumbers:list[int]):
    if len(listOfNumbers)==1:
        return listOfNumbers[0];
    else:
        return listOfNumbers[0]+sumOfList(listOfNumbers[1:])
print(sumOfList([1,2,3,4,5,6,7,8,9,10]))

#Finding the sum of nested lists using recursion
def sumOfNestedList(listOfData):
    total=0
    for i in listOfData:
        if type(i)==type([]):
            total+=sumOfNestedList(i)
        else:
            total+=i
    return total
print(sumOfNestedList([1,2,[3,4],[5,6]]))


#Finding the harmonic sum upto 'n' terms
#The harmonic sum upto 'n' terms is the sum of the reciprocals of terms from 1 to n ie 1/1 + 1/2 + 1/3 +1/4 + 1/5 +...+1/n
def harmonicSum(n):
    if n<1:
        return 0
    else:
        return 1/n + harmonicSum(n-1)

print(harmonicSum(4))

#Recursive function to solve the tower of Hanoi
def towerOfHanoi(numberofdisks,source,target,auxiliary):
    if numberofdisks==1:
        print(f"Move disk 1 from {source} to {target}")
        return
    else:
        towerOfHanoi(numberofdisks-1,source,auxiliary,target)
        print(f"Move disk {numberofdisks} from {source} to {target}")
        towerOfHanoi(numberofdisks-1,auxiliary,target,source)

towerOfHanoi(3,'A','C','B')#Move 3 disks from A to C using B as the helper
#Move 2 disks from A to B using C
#Move disk 3 from A to C
#Move 2 disks from B to C

#Questions
#1.Define a recursive function that takes two integers as input and returns their product through repeated addition instead of multiplication
def productUsingRecursiveAddition(a,b):
    if b==0:
        return 0
    elif b>0:
        return a + productUsingRecursiveAddition(a, b - 1)
    else:
        return -productUsingRecursiveAddition(a,-b)#If b is negative, we compute the product as if it were positive then we negate the result

#2.Define a recursive function that raises a base to an exponent without using the exponentiation operator
def exponentUsingRecursiveMultiplication(base,exponent):
    if exponent==0:
        return 1
    elif exponent>0:
        return base * exponentUsingRecursiveMultiplication(base,exponent-1)
    else:
        return 1/exponentUsingRecursiveMultiplication(base,-exponent)# If the exponent is negative we compute the exponentiation as if it were positive then we find the reciprocal

#3.Implement a recursive function that prints integers from a given number down to 0
def outputNumbersInDescendingOrder(startingpoint):
    if startingpoint==0:
        print(0)
    else:
        print(startingpoint,end=" ")
        outputNumbersInDescendingOrder(startingpoint-1)

#4.Implement a recursive function that prints integers from 0 upwards to a given number
def outputNumbersInAscendingOrder(endpoint,startingpoint=0):
    if startingpoint==endpoint:
        print(endpoint)
    else:
        print(startingpoint,end=" ")
        outputNumbersInAscendingOrder(endpoint,startingpoint+1)

#5.Write a recursive function that takes a string as an input and returns a reversed string using concatenation
def reverseString(string:str):
    if len(string)==0:
        return ""
    else:
        return reverseString(string[1:])+string[0]

#6.Write a recursive function that determines whether a given integer is a prime number using integers less than itself
def primeNumberValidation(number,divisor=None):
    if number<=1:
        return False
    if divisor is None:
        divisor=number-1
    if divisor==1:
        return True
    if number%divisor==0:
        return False
    return primeNumberValidation(number,divisor-1)

#7.Write a recursive function that computes the nth number of the Fibonacci sequence
@lru_cache(maxsize=128)#The maxsize parameter is the maximum number of recent function calls to cache
def Fibonacci(nthnumberofthesequence:int):
    if nthnumberofthesequence==1:
        return 0
    elif nthnumberofthesequence==2:
        return 1
    else:
        return Fibonacci(nthnumberofthesequence-1)+Fibonacci(nthnumberofthesequence-2)



