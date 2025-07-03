"""
Radix sort is a non-comparison-based integer sorting algorithm that sorts data with integer keys by grouping them by the individual digits which share the same significant position.
It works by processing the input numbers digit by digit, starting from the least significant digit and moving towards the most significant digit.
In each pass, it uses a stable sorting algorithm (like counting sort) to sort the numbers based on the value of the current digit, placing them into "buckets" for each possible digit (0-9).
Because this bucketing process is stable and is repeated for every digit position, the list becomes fully sorted once the most significant digit has been processed. Radix sort is highly efficient for large sets of integers or strings as its time complexity is linear with respect to the number of elements and the number of digits.
"""
def countingSortByDigit(array,digitPlace):
    count=[0]*10
    output=[0]*len(array)

    for number in array:
        digit=(number//digitPlace)%10
        count[digit]+=1

    for i in range(1,10):
        count[i]+=count[i-1]

    for i in range(len(array)-1,-1,-1):
        digit=(array[i]//digitPlace)%10
        output[count[digit]-1]=array[i]
        count[digit]-=1

    return output

def radixSort(array):
    if not array:
        return array

    maxNumber=max(array)
    digitPlace=1
    while maxNumber//digitPlace >0:
        array=countingSortByDigit(array,digitPlace)
        digitPlace*=10

    return array

if __name__=="__main__":
    print(radixSort([170, 45, 75, 90, 802, 24, 2, 66]))