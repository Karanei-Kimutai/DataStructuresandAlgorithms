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




fibonacciCache={}
def fibonacciversion2(n:int):
    if n in fibonacciCache:
        return fibonacciCache[n]
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        value=fibonacciversion2(n-1)+fibonacciversion2(n-2)
    fibonacciCache[n]=value
    return value

for i in range(10):
    print(f"{i}:{fibonacciversion2(i)}")





@lru_cache(maxsize=100)
def fibonacciversion3(nthnumberofthesequence:int):
    if nthnumberofthesequence==1:
        return 0
    elif nthnumberofthesequence==2:
        return 1
    else:
        return fibonacci(nthnumberofthesequence-1)+fibonacci(nthnumberofthesequence-2)

for i in range(10):
    fibonacciversion3(i)

