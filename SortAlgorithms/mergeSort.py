"""
Merge sort is a highly efficient, divide-and-conquer sorting algorithm that works by recursively breaking down a list into smaller sub-lists until each sub-list contains only one element, which is inherently sorted.
It then repeatedly merges these sorted sub-lists back together in the correct order until a single, fully sorted list is produced.
The core of the algorithm is the "merge" step, where it systematically compares the elements of two sorted sub-lists and combines them into a new, larger sorted list.
Because it consistently divides the list in half, its performance is very predictable and significantly faster than simpler algorithms like bubble or selection sort, especially for large datasets.
"""
def mergeSort(array):
    if len(array)<=1:
        return array
    else:
        middleIndex=len(array)//2 #Returns the quotient
        leftHalf=mergeSort(array[:middleIndex])
        rightHalf=mergeSort(array[middleIndex:])
        return merge(leftHalf,rightHalf)

def merge(leftHalf,rightHalf):
    sortedArray=[]
    leftIndex=rightIndex=0
    while leftIndex<len(leftHalf) and rightIndex<len(rightHalf):
        if leftHalf[leftIndex]<rightHalf[rightIndex]:
            sortedArray.append(leftHalf[leftIndex])
            leftIndex+=1
        else:
            sortedArray.append(rightHalf[rightIndex])
            rightIndex+=1

    sortedArray.extend(leftHalf[leftIndex:])
    sortedArray.extend(rightHalf[rightIndex:])
    return sortedArray

if __name__=="__main__":
    demonstrationArray=[10,9,8,7,6,5,4,3,2,1,0]
    print(mergeSort(demonstrationArray))
