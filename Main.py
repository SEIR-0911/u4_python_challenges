# Python Challenges


#  1) The Time Stone: Lets get cosmic here and begin working with Time.

# - First, lets create a function that converts Minutes to Seconds (1 ->60, 5 -> 300)
# -  Then take it up a step further, converting Hours into seconds (1 -> 3600)
# -  We're on the right track here, how many seconds are in a day
# - How many Hours are in the month of June? 
# - How many Minutes are in the month of August?
 
 # Bonus -> Without singing the old showtune in your head, how many Minutes are there in a year? 
 # In days, in weeks, in cups of coffee?
 # How are you going to tell me to not sing the song, and then type the lyrics in anyways? tsk tsk tsk.


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------

seconds_in_a_minute = 60
seconds_in_a_hour = (seconds_in_a_minute * 60)
seconds_in_a_day = (seconds_in_a_hour * 24)

days_in_January = 31
days_in_June = 30

print(seconds_in_a_day)

minutes_in_a_hour = 60
minutes_in_a_day = (minutes_in_a_hour * 24)
minuntes_in_a_year = (minutes_in_a_day * 365)

print(minuntes_in_a_year)

#  2) Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------
def mid(string):
    length = len(string)
    if length % 2 == 0 or length == 0:
        return "emptry string lol"
    else:
        middle_index = length // 2
        return string(middle_index)

middle = "abcd"

print(mid(middle))

# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "1234567894444", then it should return "*********4444".


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------
def hide_cc(card_number):
    if isinstance(card_number, str) and len(card_number) >= 4:
        asterisks = '*' * (len(card_number) - 4)
        hidden_numbers = asterisks + card_number[-4:]
        return hidden_numbers
    else: 
        return "Invalid"

print(hide_cc("4207123412341234"))


# ### 4) Online status
# The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

# For example, consider the following dictionary:

# ```
statuses = {
    "John": "online",
    "Paul": "offline",
    "George": "online",
    "Ringo": "offline"
}

# ```

# In this case, the number of people online is 2.
# Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
# Your function should return the number of people who are online.


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------
def status(d):
    num = 0
    for key in d:
        if d[key] == "online": num += 1
        return num

online_status = status(statuses)
print(online_status)

#  5) Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------
def discount(tot, percent):
    per = percent * 0.01
    discount = tot * per
    total = tot - discount
    return total

print(discount(50,10))

#  6) Pythagorean Theorum

# As any High School sophomore will tell you, the sum of the squares of two legs of a right trangle will equal the square of the hypotenouse.
# Create a function that takes two integers as the Adjacent and Opposite legs of a triangle, and returns an integer of the Hypotenouse


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------
import math

def find_hypotenouse(adjacent, opposite):
    hypotenouse = math.sqrt(adjacent**2 + opposite**2)
    return hypotenouse

adjacent_leg = 3
opposite_leg = 4
hypotenouse = find_hypotenouse(adjacent_leg, opposite_leg)
print(hypotenouse)

#  7) Fibonacci Sequence 
# Everyone's favorite Math Problem!

# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation between two adjacent steps in a list
# Create a python function that takes two numbers and finds the next Nine intervals using the Fibonacci Sequence

# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------
def fibonacci_sequence(a, b):
    sequence = [a, b]
    for _ in range(2, 11):
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    return sequence

first_num = 0
second_num = 1
final = fibonacci_sequence(first_num, second_num)
print(final)