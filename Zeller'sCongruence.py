'''
Zeller's Congruence is an algorithm used to calculate the day of the week for any date
For the Gregorian calendar, the formula is given as
  :h = ( d + [(13(m+1))/5] + K + [K/4] + [J/4] + 5J ) % 7
Where:
   d=day of the month
   m=number of the month on the calendar
   y=year
   N/B:January and February are taken as the 13th and 14th months of the previous year
   h=day of the week(0-Saturday,1-Sunday...6-Friday)
   J=century(year//100)
   K=year of the century(year%100)
Example: What day was July 4,1776
   d=4
   m=7
   y=1776
   J=1776//100= 17
   K=1776%100= 76
   h(day of the week)=(4 +[(13(7+1))/5] +76 +[76/4] +[17/4] +5*17)%7
   h=5
   5->Thursday
'''
#Python implementation
class DateCalculator:
    def __init__(self,day:int,month:int,year:int):
        self.daysOfTheWeek=["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
        self.day=day
        if month<3:
            self.month=month+12
            self.year=year-1
        else:
            self.month= month
            self.year=year

    def getDay(self):
        K=self.year%100
        J=self.year//100
        day=(self.day + (13*(self.month+1))//5 + K + (K//4) + J//4 + 5*J)%7
        return self.daysOfTheWeek[day]

datecalculator1=DateCalculator(8,7,2006)
print(datecalculator1.getDay())