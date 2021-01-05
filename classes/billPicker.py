import random

namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(", ")

nums = len(names)

choiceR = random.randint(0, nums - 1)
personPaying = names[choiceR]
print(personPaying + " is going to buy the meal today. ")


