"""
Bubble sort is a straightforward sorting algorithm that repeatedly steps through a list, compares each pair of adjacent elements, and swaps them if they are in the wrong order.
This process is repeated for each element, causing the largest unsorted values to gradually "bubble up" to their correct position at the end of the list with each pass.
The algorithm continues making these passes until a full pass is completed with no swaps, which signifies that the list is fully sorted.
While it is simple to understand and implement, bubble sort is highly inefficient for most real-world applications due to its poor performance on large lists.
"""
def bubbleSort(array):
    for passNumber in range(len(array)-1):
        swapped=False
        for currentIndex in range(len(array)-1-passNumber):
            if array[currentIndex]>array[currentIndex+1]:
                array[currentIndex],array[currentIndex+1]=array[currentIndex+1],array[currentIndex]
                swapped=True
        if not swapped:
            break
    return array

if __name__=="__main__":
    print(bubbleSort([5,1,4,2,8]))
    