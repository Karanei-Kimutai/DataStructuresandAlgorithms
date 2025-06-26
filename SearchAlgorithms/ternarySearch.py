"""
Ternary search is a divide-and-conquer searching algorithm that improves upon binary search by dividing a sorted array into three parts instead of two.
It works by calculating two middle points, mid1 and mid2, which split the current search range into three equal-sized blocks.
By comparing the target value to the elements at these two middle points, the algorithm can eliminate two-thirds of the array from consideration in a single step, narrowing down the search to the one block where the element must reside.
Although it makes more comparisons per iteration than binary search, it's particularly effective for functions where the cost of evaluating the probe position is very high, but it's less common for simple array searching because binary search typically remains more efficient in practice.
"""
from SearchAlgorithms.sortArrayAlgorithm import mergeSort


def ternarySearch(array,targetValue,leftIndex,rightIndex):
    if leftIndex>rightIndex:
        return "Value not found"
    else:
        oneThird=(rightIndex-leftIndex)//3
        middlePoint1=leftIndex+oneThird
        middlePoint2=rightIndex-oneThird
    if array[middlePoint1]==targetValue:
       return f"Value found at position {middlePoint1}"
    if array[middlePoint2]==targetValue:
        return f"Value found at position {middlePoint2}"
    if targetValue<array[middlePoint1]:
        return ternarySearch(array,targetValue,leftIndex,middlePoint1-1)
    elif targetValue>array[middlePoint2]:
        return ternarySearch(array,targetValue,middlePoint2+1,rightIndex)
    else:
        return ternarySearch(array,targetValue,middlePoint1+1,middlePoint2-1)

def startTernarySearch(array,targetValue):
    sortedArray=mergeSort(array)
    return ternarySearch(sortedArray,targetValue,0,len(sortedArray)-1)

if __name__=="__main__":
    numbers=[40, 10, 70, 20, 30, 60, 50]
    print(mergeSort(numbers))
    print(startTernarySearch(numbers,60))
    print(startTernarySearch(numbers,25))
