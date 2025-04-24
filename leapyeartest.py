#"while True" is an infinite loop because True is always true
while True:
    try:
      year=int(input("Enter the year you want to test: "))
      break
    except ValueError:
      print("Invalid input,please try again")

#Conditions for a year to be a leap year
#The year has to be divisible by 4
#Then, the year either has to be divisible by both 100 and 400 or neither
if year%4==0:
    if year%100==0 and year%400==0:
        print("The year is a leap year")
    elif year%100==0 and year%400!=0:
        print("The year is not a leap year")
    else:
        print("This is a leap year:")

else:
    print("This is not a leap year")


#Bing Chilling