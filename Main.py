import math

# Python Challenges


#  1) The Time Stone: Lets get cosmic here and begin working with Time.

# - First, lets create a function that converts Minutes to Seconds (1 ->60, 5 -> 300)
# -  Then take it up a step further, converting Hours into seconds (1 -> 3600)
# -  We're on the right track here, how many seconds are in a day
# - How many Hours are in the month of June? 
# - How many Minutes are in the month of August?
 
 
 # Bonus -> Without singing the old showtune in your head, how many Minutes are there in a year? 
 # In days, in weeks, in cups of coffee?


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------




def min_to_sec(min): 
    return min * 60


def hours_to_sec(hours): 
    return hours * 60 *60

def days_to_hours(days):
    return days * 24

def days_to_min(days):
    return days * 24 * 60

print('1) The Time Stone: ')
print('How many seconds are in a day: {}'.format(hours_to_sec(24)))
print('How many Hours are in the month of June? {}'.format(days_to_hours(30)))
print('How many Minutes are in the month of August? {}'.format(days_to_min(31)))
print('how many Minutes are there in a year?  {}'.format(days_to_min(365)))

#  2) Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------

def mid(str):
    str_len = len(str)
    if (str_len % 2 == 1):
        return str[int(str_len/2)]
    else:
        return ""

print('2) Middle letter')        
print(mid('124567'))
print(mid('12456'))

# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. 
# For example, if the function gets sent "1234567894444", then it should return "*********4444".


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------

def hide_credit_card(credit_card_num):    
    return '*' * (len(credit_card_num)-4) + credit_card_num[-4:]

print('3) Hide the credit card number', hide_credit_card('1234567890'))

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


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------

statuses = {
    "John": "online",
    "Paul": "offline",
    "George": "online",
    "Ringo": "offline"
}

def online_count(statuses):
    count = 0
    for status in statuses.values():
        if status == 'online':
            count += 1
    return count

print('4) Online status ', online_count(statuses))

#  5) Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------

def calc_discount(price, discount_percentage):
    return price -  (price * (discount_percentage/100))

print('5) Give me the discount', calc_discount(99, 20))

#  6) Pythagorean Theorum

# As any High School sophomore will tell you, the sum of the squares of two legs of a right trangle will equal the square of the hypotenouse.
# Create a function that takes two integers as the Adjacent and Opposite legs of a triangle, and returns an integer of the Hypotenouse


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------

def calc_hypot(side1, side2):
    return math.sqrt((side1*side1) + (side2*side2))

print('6) Pythagorean Theorum', calc_hypot(16, 5))

#  7) Fibonacci Sequence 
# Everyone's favorite Math Problem!

# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation between two adjacent steps in a list
# Create a python function that takes two numbers and finds the next Nine intervals using the Fibonacci Sequence

# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------

def get_fibonacci(num1, num2):
    nums = [num1, num2]
    for i in range(9):    
        nums.append(nums[-2]+nums[-1])
    return nums
print('7) Fibonacci Sequence ', get_fibonacci(4, 5))
