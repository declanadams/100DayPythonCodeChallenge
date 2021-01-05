print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

namesAdded = name1 + name2
lower_namesAdded = namesAdded.lower()

t = lower_namesAdded.count("t")
r = lower_namesAdded.count("r")
u = lower_namesAdded.count("u")
e = lower_namesAdded.count("e")

true = t + r + u + e

l = lower_namesAdded.count("l")
o = lower_namesAdded.count("o")
v = lower_namesAdded.count("v")
e = lower_namesAdded.count("e")

love = l + o + v + e


love_score = int(str(true) + str(love))


if love_score < 10 or love_score > 90:
    print(f"Your love score is {love_score}")
elif love_score >= 40 and love_score <= 50:
    print(f"your score is {love_score}")
else:
    print(f"your score is {love_score}")    
