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
