#Tip calculator, accepts total of bill , percentage of tip and amount of people splitting

                
print("Welcome to the tip calculator")

totalBill = float(input("what was the total bill?\n R"))
percentage = int(input("what percentage would you like to give? 10, 12, or 15?\n"))
people = int(input("how many people to split the bill?\n"))

tipBill = totalBill * (1 + percentage / 100)

perPerson = round(tipBill / people , 2)




print(f"Each person should pay: R {perPerson}")

        
 

