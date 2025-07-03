"""
Quick sort is a highly efficient, divide-and-conquer sorting algorithm that works by selecting a 'pivot' element from an array and partitioning the other elements into two sub-arrays according to whether they are less than or greater than the pivot.
The pivot is then placed in its final sorted position. This partitioning process is then applied recursively to the sub-arrays of elements with smaller and larger values.
The algorithm's effectiveness comes from the fact that once the pivot is positioned, it doesn't need to be moved again, and the sub-arrays can be sorted independently.
While its average-case performance is excellent, making it one of the fastest sorting algorithms in practice, its efficiency is dependent on the choice of the pivot, with a poor pivot selection potentially leading to significantly slower performance.
"""
def quickSort(array):
    if len(array)<=1:
        return array
    else:
        pivot=array[0]
        leftPartition=[]
        rightPartition=[]
        for index in range(1,len(array)):
            currentValue=array[index]
            if currentValue<=pivot:
                leftPartition.append(currentValue)
            else:
                rightPartition.append(currentValue)
        sortedLeftPartition=quickSort(leftPartition)
        sortedRightPartition=quickSort(rightPartition)
        sortedArray=[]
        for value in sortedLeftPartition:
            sortedArray.append(value)
        sortedArray.append(pivot)
        for value in sortedRightPartition:
            sortedArray.append(value)

        return sortedArray

if __name__=="__main__":
    numbers=[10, 7, 8, 9, 1, 5]
    print(quickSort(numbers))
