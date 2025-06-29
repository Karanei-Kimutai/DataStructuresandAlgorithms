from SearchAlgorithms.sortArrayAlgorithm import mergeSort
def recursiveBinarySearch(sortedArray,targetValue,startIndex,endIndex):
    if startIndex>endIndex:
        return "Value not found"

    middleIndex=(startIndex+endIndex)//2
    middleValue=sortedArray[middleIndex]
    if middleValue==targetValue:
        return f"Value found at position {middleIndex} of the sorted array"
    elif middleValue>targetValue:
        return recursiveBinarySearch(sortedArray,targetValue,startIndex,middleIndex-1)
    else:
        return recursiveBinarySearch(sortedArray,targetValue,middleIndex+1, endIndex)

if __name__=="__main__":
    numbers=[12, 5, 8, 19, 1, 3, 17]
    sortedNumbers=mergeSort(numbers)
    print(sortedNumbers)
    print(recursiveBinarySearch(sortedNumbers,10,0,len(sortedNumbers)-1))

