"""
Binary Search is an efficient algorithm that works only on sorted arrays.
It begins by comparing the target to the middle element. If they match, the search ends.
If the target is smaller, the algorithm repeats the process on the left half of the array; if larger, on the right half.
This halves the search space with each step, making it much faster than linear search.
Binary Search is best when you have frequent queries on a sorted dataset.
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

if __name__=="__main__":
    numbers=[10,2,8,4,1,9,11,4]
    print(mergeSort(numbers))
    print(binarySearch(numbers,11))