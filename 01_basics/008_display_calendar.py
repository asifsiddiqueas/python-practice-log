#Program to display the calendar

import calendar

#user defined month and Year
year = int(input("Enter your Year: "))
month = int(input("Enter your month (1-12): "))

#Defining function in cal variable
if year <= 0:
    print("Invalid Year! Please Enter a positive year")
elif 1 <= month <= 12:
    cal = calendar.month(year, month)
    print(cal)
else:
    print("Invalid month! please enter a value between 1-12")