#1. After flipping a coin 10 times you got this result,
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# Using for loop figure out how many times you got heads

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count = 0
for i in result:
    if i =="heads":
        count += 1
print(count)

# 2.Print square of all numbers between 1 to 10 except even numbers

for i in range(1 , 10, 2):
    print(i*i)
    
# 3.Your monthly expense list (from Jan to May) looks like this,
# expense_list = [2340, 2500, 2100, 3100, 2980]
# Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred.
# If expense is not found then it should print that as well.

expense_list = [2340, 2500, 2100, 3100, 2980]
amount = int(input("enter the expense amount :- "))
for index , value in enumerate(expense_list):
    if value == amount:
        print(index)
        break
else :
        print ("not found")
        
# 4.Lets say you are running a 5 km race. Write a program that,
# Upon completing each 1 km asks you "are you tired?"
# If you reply "yes" then it should break and print "you didn't finish the race"
# If you reply "no" then it should continue and ask "are you tired" on every km
# If you finish all 5 km then it should print congratulations message


for i in range(5):
    user = input(("are you tired?:- "))
    if user == "yes":
        print("you didn't finish the race")
        break
    elif i == 4 :
        print("congratulations you finish all 5 km")
    elif user == "no":
        continue
    
    
# 5.Write a program that prints following shape
# *
# **
# ***
# ****

star = "*"
for i in range(1,6):
    print(star*i)
