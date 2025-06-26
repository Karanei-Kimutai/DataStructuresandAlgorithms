"""
A jump search is an efficient searching algorithm for sorted arrays that works by "jumping" forward in fixed-size steps instead of checking every element sequentially.
It repeatedly leaps ahead by a set block size (often the square root of the array's length) until the element at the jump point is greater than the target value.
Once this happens, the algorithm knows the target must lie within the previous block it just jumped over.
It then performs a simple linear search within that smaller, specific block to pinpoint the exact location of the element, significantly reducing the total number of comparisons compared to a standard linear search.
"""
import math
from SearchAlgorithms.sortArrayAlgorithm import mergeSort


def jumpSearch(array,targetValue):
    sortedArray=mergeSort(array)
    arrayLength=len(sortedArray)
    jumpStep=int(math.sqrt(arrayLength))
    previousIndex=0

    while previousIndex<arrayLength and sortedArray[min(jumpStep,arrayLength)-1]<targetValue:
        previousIndex=jumpStep
        jumpStep+=int(math.sqrt(arrayLength))
        if previousIndex>=arrayLength:
            return f"Value not found"
    for currentIndex in range(previousIndex,min(jumpStep,arrayLength)):
        if sortedArray[currentIndex]==targetValue:
            return f"Value found at index: {currentIndex}"
    return f"Value not found"


if __name__=="__main__":
    numbers=[9,6,7,3,2,1,11,10,15,5]
    print(mergeSort(numbers))
    print(jumpSearch(numbers,7))