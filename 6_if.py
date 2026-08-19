# Exercise: Python If Condition

# Using following list of cities per country,
# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]
# 1.Write a program that asks user to enter a city name and it should tell which country the city belongs to
# 2.Write a program that asks user to enter two cities and it tells you if they both are in same country or not.
# For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and 
# dhaka it should print "They don't belong to same country"

# 1.answer
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city = input("enter the city name :- ")
if city.lower() in india:
    print(f"{city} belongs to india")
elif city in pakistan:
    print(f"{city} belongs to pakistan")
elif city in bangladesh:
    print(f"{city} belongs to bangladesh")
else:
    print("plz enter valid city name")
    
# 2.answer

city1 = input("enter the 1st city name :- ")
city2 = input("enter the 2nd city name :- ")

if city1.lower() and city2.lower() in india:
    print(f"{city} belongs to india")
elif city1.lower() and city2.lower() in pakistan:
    print(f"{city} belongs to pakistan")
elif city1.lower() and city2.lower() in bangladesh:
    print(f"{city} belongs to bangladesh")
else:
    print("plz enter valid city name")

# Write a python program that can tell you if your sugar is normal or not. 
# Normal fasting level sugar range is 80 to 100.
# Ask user to enter his fasting sugar level
# If it is below 80 to 100 range then print that sugar is low
# If it is above 100 then print that it is high otherwise print that it is normal

suger_range = int (input("enter your fasting sugar level :- "))
if suger_range < 80 :
    print ("sugar is low")
elif suger_range > 100 :
    print("suger is high")
else :
    print("suger is normal")