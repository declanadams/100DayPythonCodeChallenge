print("hello lets get your order!")


size = input("Enter size S, M or L\n")
addP = input("Add pepperoni Y or N\n")
addC = input("Add extra cheese Y or N\n")

bill= 0


if size == "S":
    bill = 15

    if addP == "Y":
        bill += 2
    else:
        bill = 15

        if addC == "Y":
            bill += 1

elif size == "M":
    bill = 20 

    if addP == "Y":
        bill += 3
    else:
        bill = 20 

        if addC == "Y":
            bill += 1  
        
else:
    bill = 25

    if addP =="Y":
        bill += 3
    else:
        bill = 25    

        if addC == "Y":
            bill += 1


print(f"Your final bill is: {bill}")            

   
