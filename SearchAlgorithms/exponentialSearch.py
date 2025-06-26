"""
Exponential search is a highly efficient algorithm for searching in sorted, unbounded, or infinitely large arrays.
It operates in two stages: first, it determines a range where the target value is likely to be by "jumping" through the array in exponentially increasing steps (checking indices 1, 2, 4, 8, 16, and so on) until it finds an index where the element is greater than the target.
Once this upper bound is found, the algorithm knows the target must lie in the previous, smaller block.
For the second stage, it performs a standard binary search on this identified block to pinpoint the exact location of the element, combining exponential growth to find the range with the precision of binary search to find the value.
"""
from SearchAlgorithms.sortArrayAlgorithm import mergeSort


def binarySearch(array,targetValue):
    sortedArray=mergeSort(array)
    startIndex=0
    endIndex=len(sortedArray)-1
    while startIndex<=endIndex:
        middleIndex=(startIndex+endIndex)//2
        middleValue=sortedArray[middleIndex]
        if middleValue==targetValue:
            return f"Value found at position {middleIndex} of the sorted array"
        elif middleValue<targetValue:
            startIndex=middleIndex+1
        else:
            endIndex=middleIndex-1
    return "Value not found"

def exponentialSearch(array,targetValue):
    sortedArray=mergeSort(array)
    if sortedArray[0]==targetValue:
        return f"Value found at position {0}"
    else:
        index=1
        while index<len(sortedArray) and sortedArray[index]<=targetValue:
            index*=2
        return binarySearch(sortedArray[:min(index,len(sortedArray))],targetValue)

if __name__=="__main__":
    numbers=[12, 3, 7, 1, 9, 4, 18, 5]
    print(mergeSort(numbers))
    print(exponentialSearch(numbers,18))
    print(exponentialSearch(numbers,11))

