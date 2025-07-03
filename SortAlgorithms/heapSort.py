"""
Heap sort is an efficient, comparison-based sorting algorithm that leverages a binary heap data structure to sort elements.
The algorithm is typically performed in two main phases:
First, it transforms the input list into a max heap, which is a specialized tree-based structure where the value of each parent node is greater than or equal to the values of its children, ensuring the largest element is at the root.
In the second phase, it repeatedly extracts the maximum element from the root of the heap, places it at the end of the sorted portion of the array, and then reconstructs the heap with the remaining elements.
This process of extracting the max element and restoring the heap property continues until all elements have been moved from the heap to the sorted array, resulting in a fully sorted list.
"""
def heapify(array,heapSize,rootIndex):
    largest=rootIndex
    leftChild=2*rootIndex+1
    rightChild=2*rootIndex+2
    if leftChild<heapSize and array[leftChild]>array[largest]:
        largest=leftChild
    if rightChild<heapSize and array[rightChild]>array[largest]:
        largest=rightChild
    if largest !=rootIndex:
        array[rootIndex],array[largest]=array[largest],array[rootIndex]
        heapify(array,heapSize,largest)

def heapSort(array):
    n=len(array)
    for i in range(n//2 -1,-1,-1):
        heapify(array,n,i)
    for i in range(n-1,0,-1):
        array[0],array[i]=array[i],array[0]
        heapify(array,i,0)
    return array

if __name__=="__main__":
    print(heapSort([12,11,13,5,6,7]))