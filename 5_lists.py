# Exercise: Python Lists

# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

monthly_expenses = [2200,2350,2600,2130,2190]

# 1.answer
print(f"In Feb, {monthly_expenses[1]-monthly_expenses[0]} dollars spent extra compare to January")

# 2.answer
print(f"total expens in first quarter of the year is {monthly_expenses[0]+ monthly_expenses[1]+monthly_expenses[2]}")

# 3.answer
for index , value in enumerate(monthly_expenses):
    if value == 2000:
        print(index)
else :
    print("you does not spent exactly 2000 dollars in any month")
    
# 4.answer
monthly_expenses.append(1980)
print(monthly_expenses)

# 5.answer
monthly_expenses[3]=1930
print(monthly_expenses)

# You have a list of your favourite marvel super heros.
# heros=['spider man','thor','hulk','iron man','captain america']
# Using this find out,

# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

heros=['spider man','thor','hulk','iron man','captain america']

# 1.answer
print(len(heros))

# 2.answer
heros.append("black panther")
print(heros)

# 3.answer
heros.remove("black panther")
print(heros)
heros.insert(3,"black panther")
print(heros)

# 4.answer
heros[1:3]=["doctor strange"]
print(heros)

#5.answer
heros.sort()
print(heros)
