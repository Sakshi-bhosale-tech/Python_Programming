# Exercise: Python Dict and Tuples
# We have following information on countries and their population (population is in crores),

# Country	Population
# China	143
# India	136
# USA	32
# Pakistan	21
# Using above create a dictionary of countries and its population
# Write a program that asks user for three type of inputs,
# print: if user enter print then it should print all countries with their population in this format,
# china==>143
# india==>136
# usa==>32
# pakistan==>21
# add: if user input add then it should further ask for a country name to add. 
# If country already exist in our dataset then it should print that it exist and do nothing. 
# If it doesn't then it asks for population and add that new country/population in our dictionary and print it
# remove: when user inputs remove it should ask for a country to remove. 
# If country exist in our dictionary then remove it and print new dictionary using format shown above in (a). 
# Else print that country doesn't exist!
# query: on this again ask user for which country he or she wants to query. When user inputs that country it will print population of that country.

info = {"China":143 , "India": 136, "USA":32, "Pakistan" : 21 }


while True :
    print ("---Menu---\n 1.print \n 2.add \n 3.remove \n 4.query\n 5.exits\n")
    a = int(input("enter the the option :- "))
    if a == 1:
        for c ,p in info.items():
            print(f"{c}==>{p}")
    elif a == 2:
        new_name = input("enter country name to add :- ")
        if new_name in info.keys() :
            print("it alredy exist")
        else :
            new_p = int(input("enter the population"))
            info[new_name]=new_p
            print(info)
        
    elif a == 3:
        to_remove = input("enter the country to remove")
        if to_remove in info.keys():
            info.pop(to_remove)
            for c , p in info.items():
                print(f"{c}==>{p}")
        else:
            print("country doesn't exist!")
    elif a == 4:
        c = input("enter which country you want to query")
        if c in info:
            print(info[c])
        else:
            print("Country doesn't exist!")
    elif a == 5:
        print("Program exited.")
        break
    else:
        print("enter valid option ")
    
    
# You are given following list of stocks and their prices in last 3 days,
# Stock	Prices
# info	[600,630,620]
# ril	[1430,1490,1567]
# mtl	[234,180,160]
# Write a program that asks user for operation. Value of operations could be,
# print: When user enters print it should print following,
# info ==> [600, 630, 620] ==> avg:  616.67
# ril ==> [1430, 1490, 1567] ==> avg:  1495.67
# mtl ==> [234, 180, 160] ==> avg:  191.33
# add: When user enters 'add', it asks for stock ticker and price. 
# If stock already exist in your list (like info, ril etc) then it will append the price to the list.
# Otherwise it will create new entry in your dictionary. For example entering 'tata' 
# and 560 will add tata ==> [560] to the dictionary of stocks. 
import statistics
Info = {"info":[600,630,620] ,"ril" :[1430,1490,1567] ,"mtl":[234,180,160]}

print ("---Menu---\n 1.print \n 2.add ")
a = int(input("enter the the option :- "))
    
if a == 1:
    for c ,p in Info.items():
        avg = statistics.mean(p)
        print(f"{c}==>{p}  ==> avg: ",round(avg,2))
elif a == 2:
    new_name = input("Enter a stock ticker to add:-  ")
    p = input("Enter price of this stock:")
    if new_name in Info :
        Info[new_name].append(p)
    else :
        Info[new_name]= p
        print(Info)
        
# Write circle_calc() function that takes radius of a circle as an input from user and 
# then it calculates and returns area, circumference and diameter. 
# You should get these values in your main program by calling circle_calc function and 
# then print them 

import math

def circle_calc(radius):
    area=math.pi*(radius**2)
    circumference=2*math.pi*radius
    diameter=2*radius
    return area, circumference,diameter

if __name__=="__main__":
    r=input("Enter a radius:")
    r=float(r)
    area, c, d = circle_calc(r)
    print(f"area {area}, circumference {c}, diameter {d}")