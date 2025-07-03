"""
Counting sort is a highly efficient, non-comparison-based sorting algorithm that works by determining, for each element in the input list, the number of elements that are less than it.
It operates under the constraint that the input consists of integers within a specific, known range.
The algorithm creates a temporary "count" array to store the frequency of each unique element and then transforms this count array to hold the cumulative sum of frequencies, which directly gives the final sorted position for each element.
Because it doesn't compare elements to each other, counting sort can be significantly faster than comparison-based algorithms like quick sort or merge sort, but it is only suitable for data with a relatively small range of integer values.
"""
def countingSort(array):
    if len(array)==0:
        return array
    maximumValue=array[0]
    #Find the maximum value in the array
    for index in range(1,len(array)):
        if array[index]>maximumValue:
            maximumValue=array[index]

    countArray=[]
    for index in range(maximumValue+1):
        countArray.append(0)
    #Count each element's frequency
    for index in range(len(array)):
        currentValue=array[index]
        countArray[currentValue]=countArray[currentValue]+1

    sortedArray=[]
    for value in range(len(countArray)):
        frequency=countArray[value]
        for repeat in range(frequency):
            sortedArray.append(value)

    return sortedArray


if __name__=="__main__":
    numbers=[4,2,2,8,3,3,1]
    print(countingSort(numbers))