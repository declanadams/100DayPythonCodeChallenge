# Write a program that works out whether if a given year is a leap year.
#  A normal year has 365 days, leap years have 366, with an extra day in February.
#  The reason why we have leap years is 
# really fascinating, this video does it more justice:



year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")
        else:
            print("not leap year")
    else:
        print("leap year")        
else:
    print("not leap year")    
   

        
