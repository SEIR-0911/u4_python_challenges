# Python Challenges


#  1) The Time Stone: Lets get cosmic here and begin working with Time.

# - First, lets create a function that converts Minutes to Seconds (1 ->60, 5 -> 300)
# -  Then take it up a step further, converting Hours into seconds (1 -> 3600)
# -  We're on the right track here, how many seconds are in a day
# - How many Hours are in the month of June? 
# - How many Minutes are in the month of August?
def min_to_sec(min):
    return min * 60 

def hour_to_sec(hour):
    return (hour * 60) * 60

def hour_in_month(days):
    return (days * 24) 

def min_in_month(days):
    return (days * 24) * 60

#print(hour_to_sec(24)) #86400
#print(hour_in_month(30)) #720
#print(min_in_month(31)) #44640



 
 
 # Bonus -> Without singing the old showtune in your head, how many Minutes are there in a year? 
 # In days, in weeks, in cups of coffee?
def minutes_in_year(days):
    return (days * 24) * 60

#print(minutes_in_year(365)) #525600





#  2) Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".


def mid(string):
    length = len(string)
    if length % 2 == 0 or length == 0:
        return "even or no input"
    else:
        middle_index = length // 2
        return string[middle_index]
    
midcheck1 ="abcd"
    
#print(mid(midcheck1))


# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "1234567894444", then it should return "*********4444".


def hide_credit_card(card_number):
    if isinstance(card_number, str) and len(card_number) >= 4:
        asterisks = '*' * (len(card_number) - 4)
        hidden_card = asterisks + card_number[-4:]
        return hidden_card
    else:
        return "Invalid input"
    
#print(hide_credit_card("55554445"))




# ### 4) Online status
# The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

# For example, consider the following dictionary:

# ```
# statuses = {
#     "John": "online",
#     "Paul": "offline",
#     "George": "online",
#     "Ringo": "offline"
# }

# ```

# In this case, the number of people online is 2.
# Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
# Your function should return the number of people who are online.


def status(d):
    num = 0
    for key in d:
        if d[key] == "online":
            num += 1
    return num

# result = status(statuses)
# print(result)



#  5) Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

def discoutn(tot, percent):
    perc = percent *.01
    discount = tot * perc
    final_price = tot - discount
    return final_price

#print(discoutn(50,10))

#  6) Pythagorean Theorum

# As any High School sophomore will tell you, the sum of the squares of two legs of a right trangle will equal the square of the hypotenouse.
# Create a function that takes two integers as the Adjacent and Opposite legs of a triangle, and returns an integer of the Hypotenouse


import math

def calculate_hypotenuse(adjacent, opposite):
    hypotenuse = math.sqrt(adjacent**2 + opposite**2)
    return hypotenuse


adjacent_leg = 3
opposite_leg = 4
hypotenuse = calculate_hypotenuse(adjacent_leg, opposite_leg)
print(hypotenuse)  # Output: 5.0


#  7) Fibonacci Sequence 
# Everyone's favorite Math Problem!

# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation between two adjacent steps in a list
# Create a python function that takes two numbers and finds the next Nine intervals using the Fibonacci Sequence

def fibonacci_sequence(a, b):
    sequence = [a, b]
    for _ in range(2, 11):
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence


first_number = 0
second_number = 1
result = fibonacci_sequence(first_number, second_number)
print(result)