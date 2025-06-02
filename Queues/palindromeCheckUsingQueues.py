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


userInput=input("Enter the string you want to test: ").strip().lower().replace(" ","")
palindromeCheckUsingQueues(userInput)
