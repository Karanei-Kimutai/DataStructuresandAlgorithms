"""
Insertion sort is an intuitive sorting algorithm that builds a final sorted array one element at a time.
It iterates through the input list, and for each element, it removes it from the unsorted portion and "inserts" it into its correct position within the already sorted portion by shifting all larger elements one position to the right.
This process is analogous to how many people sort a hand of playing cards, picking up one card at a time and placing it in its correct spot among the cards they are already holding. While generally inefficient for large, unsorted lists, insertion sort is very fast for small datasets and for lists that are already mostly sorted.
"""
def insertionSort(array):
    for index in range(1,len(array)):
        key=array[index]
        position=index-1
        while position>=0 and array[position]>key:
            array[position+1]=array[position]
            position-=1
        array[position+1]=key
    return array

if __name__=="__main__":
    print(insertionSort([9,5,1,4,3]))
