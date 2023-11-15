# Python Challenges


#  1) The Time Stone: Lets get cosmic here and begin working with Time.

# - First, lets create a function that converts Minutes to Seconds (1 ->60, 5 -> 300)
number_of_seconds_in_minute = 60

def convert_seconds_to_mins (min):
    
    seconds_in_minute=min*number_of_seconds_in_minute
    print(seconds_in_minute)
    
convert_seconds_to_mins(5)

# -  Then take it up a step further, converting Hours into seconds (1 -> 3600)
number_of_minutes_in_hour= 60

def seconds_in_hour (hours):
     seconds_in_hour=number_of_seconds_in_minute * hours * number_of_minutes_in_hour
     return seconds_in_hour

print(seconds_in_hour(3))

# -  We're on the right track here, how many seconds are in a day

def seconds_in_day (hours):
     seconds_in_hour=number_of_seconds_in_minute * hours * number_of_minutes_in_hour
     return seconds_in_hour
print(seconds_in_hour(3))

# - How many Hours are in the month of June? 
hours_in_day=24

def june(days):
     hours_in_june=hours_in_day * days
     print(hours_in_june)

june(30)

# - How many Minutes are in the month of August?
def august(days):
     minutes_in_august= hours_in_day*60*days
     print(minutes_in_august)
august(30)


#  2) Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".
def mid(string):
     length=len(string)
     if length % 2 > 0:
          middle_index=(length-1)//2
        #   strings support indexing like arrays do, so you can do this to find the middle letter:
          middle_number=string[middle_index]
          print(middle_number)
     else:
          print ("")

mid("hello")

# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. 
# It should return a string where all the characters are hidden with an asterisk 
# except the last four. For example, if the function gets sent "1234567894444", 
# then it should return "*********4444".

def hide_credit_card(card_number):
     if len(card_number) >= 4:
                  # Replace all characters except the last four with asterisks
        hidden_card = '*' * (len(card_number) - 4) + card_number[-4:]
        return hidden_card
     else:
        return

credit_card_number = "1234567894444"
hidden_number = hide_credit_card(credit_card_number)
print(hidden_number)


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

def online_count(dictionary):
        online_users = sum(status == "online" for status in dictionary.values())
        print(online_users)
     
dictionary1 = {
    "Alice": "online",
    "Bob": "offline",
    "Charlie": "online",
    "David": "offline"
}

online_count(dictionary1)


#  5) Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

def price(price, discount):
     price = (discount*(.01)) * price
     return price

print(price(100,80))


#  6) Pythagorean Theorum

# As any High School sophomore will tell you, the sum of the squares of two legs of a right trangle will equal the square of the hypotenouse.
# Create a function that takes two integers as the Adjacent and Opposite legs of a triangle, and returns an integer of the Hypotenouse
import math

def hyp(a, b):
    hyp=math.sqrt((a**2)+(b**2))
    return hyp

print(hyp(5,3))


#  7) Fibonacci Sequence 
# Everyone's favorite Math Problem!

# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation between two adjacent steps in a list
# Create a python function that takes two numbers and finds the next Nine intervals using the Fibonacci Sequence

# print all fibanaci numbers:

def fibonacci(num1, num2, numcount):
    num_list = [num1, num2]
    for num in range(numcount):
        num_list.append(num_list[-1] + num_list[-2])
    return num_list
print(fibonacci(0, 1, 7))

# Print the ninth Fibonacci numbe
#
def fibonacci(num1, num2, numcount):
    num_list = [num1, num2]
    for _ in range(numcount):
        num_list.append(num_list[-1] + num_list[-2])
    return num_list[-1]

print(fibonacci(0, 1, 7))

# or

def fib(num1, num2):
     num3=num1+num2
     num4=num3+num2
     num5=num3+num4
     num6=num4 + num5
     num7=num5+num6
     num8=num6+num7
     num9=num7+num8
     print(num9)

fib(0,1)

# or

def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence

result = fibonacci(9)
print(result[-1])  
# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------
