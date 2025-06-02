def palindromeCheckUsingQueues(string):
    queue=[]
    for character in string:
        queue.insert(0,character)
    reversedString="".join(queue)
    if string==reversedString:
        print("This string is a palindrome")
        return True
    else:
        print("This string is not a palindrome")
        return False

def palindromeCheckUsingQueues2(string):
    queue=[]
    for character in string:
        queue.append(character)
    reversedString=""
    while len(queue)!=0:
        reversedString+=queue.pop()
    if string == reversedString:
        print("This string is a palindrome")
        return True
    else:
        print("This string is not a palindrome")
        return False


userInput=input("Enter the string you want to test: ").strip().lower().replace(" ","")
palindromeCheckUsingQueues(userInput)
palindromeCheckUsingQueues2(userInput)
