"""
Selection sort is a simple sorting algorithm that works by repeatedly finding the minimum element from the unsorted part of a list and placing it at the beginning of the sorted part.
The algorithm divides the input list into two portions: a sorted sublist which is built up from left to right at the front, and a sublist of the remaining unsorted items.
In each pass, it scans the entire unsorted portion to find the smallest element and then swaps it with the first element of that unsorted portion, thereby growing the sorted sublist by one.
Although selection sort is noted for its simplicity and for minimizing the number of swaps required, its performance is generally poor on large lists because it must always scan the entire remaining list to find the next smallest element.
"""
def selectionSort(array):
    for i in range(len(array)):
        minIndex=i
        for j in range(i+1,len(array)):
            if array[j]<array[minIndex]:
                minIndex=j
        array[i],array[minIndex]=array[minIndex],array[i]
    return array

if __name__=="__main__":
    print(selectionSort([64,25,12,22,11]))