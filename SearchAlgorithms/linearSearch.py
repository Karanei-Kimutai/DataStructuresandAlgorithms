"""
Linear search works by looping through each element of an array from the beginning and checking if the element matches the value being sought for
"""
def linearSearch(array,targetValue):
    for currentIndex in range(len(array)):
        if array[currentIndex]==targetValue:
            return f"Value found at position[{currentIndex}]"

    return "Value not found"

if __name__=="__main__":
    demoArray=[5,2,9,1,7]
    print(linearSearch(demoArray,9))