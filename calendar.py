#calendar.py - code to print a calendar on command line
#Created by Dr. Aarathi Prasad 7/12/21
#Programmed by Azizul Hakim

import sys

#This function prints out the days in a row for the calendar
def dayrow():
    dayrow = []
    for loop in days_in_a_week:
        dayrow.append(loop[0:2])
    dayrow = ' '.join(dayrow)
    print(dayrow)

#This function checks the year whether it is a leap year or not and changes
#February to 29 days if it is a leap year
def leap(leap_check):
	if (leap_check % 400 == 0) and (leap_check % 100 == 0):
	    days_in_a_month[1] = 29
	    print(f'{leap_check} is a leap year')
	elif (leap_check % 4 ==0) and (leap_check % 100 != 0):
	    days_in_a_month[1] = 29
	    print(f'{leap_check} is a leap year')
	else:
	    print(f'{leap_check} is not a leap year')
	return leap_check

#This function returns the firstday of a month
def firstday(firstday_month,month):
    firstday_month = sum(days_in_a_month[0:(month-1)]) + first_day_of_year + 1
    firstday_number = int(firstday_month % 7)
    return firstday_number

######Task 1) Ask user to enter year
#Replace 2021 in the next statement with user entered year
year = int(input("Enter a year: "))
#Ask user to keep entering a year until they enter a value greater than 1900.
while year <= 1900:
	year = int(input("Enter a year: "))

######Task 2) Ask user to enter month (1 for January, 12 for December)
#Replace 7 with user entered month if month entered is valid (1-12)
#Ask user to keep entering a month until they enter a value between 1 and 12
month = int(input("Enter a month (1 for January, 12 for December): "))
while month not in range(1,13):
	month = int(input("Enter a month: "))
#first day of year is calculated using the following formula
#(2 + (year-1901) + (year-1901)/4) % 7
#the expression returns a float value, so we convert it to an int, so it returns
#a value 0 to 6
#if 0, it is a Sunday, 6, it is a Saturday
first_day_of_year = int((2 + (year-1901) + (year-1901)/4) % 7)
days_in_a_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

######Task 3) How will you store the names of the days of the week, so it prints Sunday instead of 0?
#I used the first_day_of_year number on the days_in_a_week list to get the days name instead of 0
print(f'First day of {year} is on a {days_in_a_week[first_day_of_year]}')

######Task 4) How will you store the names of the months and number of days in each month?
#I made a list for both months in the year to days in the month to store the values
months_in_a_year = ['January','February','March','April','May','June','July','August','September','October', 'November','December']
days_in_a_month = [31,28,31,30,31,30,31,31,30,31,30,31]

######Task 5) Check and print a message whether the year is a leap year or not
######Task 6) If it is a leap year, modify number of days in February from 28 to 29
#I did both Task 5 and 6 in a function called leapyearCheck
leapyearCheck = leap(year)

######Task 7) How will you calculate which day the 1st of month is on, now that you know which day Jan 1st falls on,
# how many number of days every month has, and whether the year is a leap year or not?
# Hint: you must use a loop here
firstday = firstday(days_in_a_month,month)


######Task 8) Print a message that clearly states which day of the week the 1st day of the user-entered month in the user-entered year starts on.
print(f'First day of {months_in_a_year[(month-1)]} {year} is on a {days_in_a_week[firstday-1]}')

###### End of Checkpoint for Week 1 #######

######Task 9) How do you print the month name and year? Do not worry about centralizing this.
print(f'\n{months_in_a_year[(month-1)]} {year}')

######Task 10) How do you print the names of days of the week programmatically? You must use a loop
#I use the loop on the dayrow function to print the names of days of the week
dayrow()
#If it is saturday, the equation gives 0, we change it to 7 to get the equivalent dashes
if firstday == 0:
    firstday = 7

#code for adding spaces in blank days of the week
n = 1
final_ls = []
while firstday > n:
    spaces = '  '
    final_ls.append(spaces)
    n=n+1

#code for adding the days of a month in the list
for i in range(1,10):
    ten_date = str(i)
    ten_date = ('0'+ten_date)
    final_ls.append(ten_date)
for i in range(10,(days_in_a_month[month-1]+1)):
    final_ls.append(str(i))

#printing the calendar through loops
n=0
for k in range(0,6):
    print(' '.join(final_ls[n:(n+7)]))
    n=n+7

#THE END
