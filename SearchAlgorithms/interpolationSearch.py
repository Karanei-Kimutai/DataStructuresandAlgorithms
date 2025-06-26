"""
Interpolation search is an enhanced searching algorithm for sorted, uniformly distributed arrays that improves upon binary search by making a more "intelligent" guess.
Instead of always checking the middle element, it probes a position based on the value it's searching for relative to the values at the ends of the array.
This is analogous to how a person searches a phone book: for a name starting with 'W', you'd open the book much closer to the end than the middle.
By estimating the likely position of the target, this method can converge on the result significantly faster than binary search on average, but its efficiency is highly dependent on the data being evenly distributed.
"""
from SearchAlgorithms.sortArrayAlgorithm import mergeSort


def interpolationSearch(array,targetValue):
    sortedArray=mergeSort(array)
    startIndex=0
    endIndex=len(sortedArray)-1
    while startIndex<=endIndex and sortedArray[startIndex]<=targetValue<=sortedArray[endIndex]:
        if sortedArray[startIndex]==sortedArray[endIndex]:
            if sortedArray[startIndex]==targetValue:
                return f"Value found at position: {startIndex}"
            else:
                return f"Value not found"

        position=startIndex+((targetValue-sortedArray[startIndex])*(endIndex-startIndex))// (sortedArray[endIndex]-sortedArray[startIndex])
        if position>=len(sortedArray):
            return f"Value not found"
        if sortedArray[position]==targetValue:
            return f"Value found at position {position}"
        elif sortedArray[position]<targetValue:
            startIndex=position+1
        else:
            endIndex=position-1
    return "Value not found"

if __name__=="__main__":
    numbers=[10,70,40,30,60,50,20]
    print(mergeSort(numbers))
    print(interpolationSearch(numbers,50))
    print(interpolationSearch(numbers,35))