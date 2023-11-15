# Python Challenges


#  1) The Time Stone: Lets get cosmic here and begin working with Time.

# - First, lets create a function that converts Minutes to Seconds (1 ->60, 5 -> 300)
# -  Then take it up a step further, converting Hours into seconds (1 -> 3600)
# -  We're on the right track here, how many seconds are in a day
# - How many Hours are in the month of June? 
# - How many Minutes are in the month of August?
# def min_to_sec(mins):
#     return mins * 60
# print(min_to_sec(5))
# def hours_to_mins(hours):
#     return hours * 60
# print(min_to_sec(hours_to_mins(1))) # ANSWER: 1 hour = 3600 seconds
# def day_to_hours(days):
#     return days * 24
# print(min_to_sec(hours_to_mins(day_to_hours(1)))) # ANSWER: 1 day = 86400 seconds
# june = 30
# august = 31
# print(day_to_hours(june)) # ANSWER: hours in June = 720
# print(hours_to_mins(day_to_hours(august))) # ANSWER: hours in august = 44640

 # Bonus -> Without singing the old showtune in your head, how many Minutes are there in a year? 
 # In days, in weeks, in cups of coffee?
# days_in_year = 365
# print(hours_to_mins(day_to_hours(days_in_year))) # ANSWER: minutes in a year: 525600 minutes

# ---------------------------------
#      Solution Goes Here ->
def min_to_sec(mins):
    return mins * 60
def hours_to_mins(hours):
    return hours * 60
def day_to_hours(days):
    return days * 24
june = 30
august = 31
days_in_year = 365
    # print(min_to_sec(5))
    # print(min_to_sec(hours_to_mins(1))) # ANSWER: 1 hour = 3600 seconds
    # print(min_to_sec(hours_to_mins(day_to_hours(1)))) # ANSWER: 1 day = 86400 seconds
    # print(day_to_hours(june)) # ANSWER: hours in June = 720
    # print(hours_to_mins(day_to_hours(august))) # ANSWER: hours in august = 44640
    # print(hours_to_mins(day_to_hours(days_in_year))) # ANSWER: minutes in a year: 525600 minutes

# ---------------------------------



#  2) Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".
# def mid(str):
#     if len(str) % 2 == 0:
#         return 'no middle'
#     else:
#         i = len(str) // 2
#         return str[i]

# print(mid('abcdefg'))

# ---------------------------------
#      Solution Goes Here -> 
def mid(str):
    if len(str) % 2 == 0:
        return 'no middle'
    else:
        i = len(str) // 2
        return str[i]
# ---------------------------------


# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "1234567894444", then it should return "*********4444".

def hide_numbers(nums):
    return '*' * (len(nums)-4) + nums[-4:]

# ---------------------------------
#      Solution Goes Here ->
def hide_numbers(nums):
    return '*' * (len(nums)-4) + nums[-4:]

# print(hide_numbers('123456789'))
# ---------------------------------



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
def online_count(people):
    count = 0
    for key in people:
        if people[key] == 'online':
            count += 1
        # print(key)
    return count

# print(online_count(statuses))
# ---------------------------------



#  5) Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

# def discount(full, dis):
#     total_discount = (full * dis) / 100
#     return full - total_discount
# ---------------------------------
#      Solution Goes Here ->
def discount(full, dis):
    total_discount = (full * dis) / 100
    return full - total_discount

# print(discount(100,20))
# ---------------------------------


#  6) Pythagorean Theorum

# As any High School sophomore will tell you, the sum of the squares of two legs of a right trangle will equal the square of the hypotenouse.
# Create a function that takes two integers as the Adjacent and Opposite legs of a triangle, and returns an integer of the Hypotenouse


# ---------------------------------
#      Solution Goes Here ->
def pythagorean(a, b):
    return ((a ** 2) + (b ** 2)) ** .5
# print(pythagorean(3,4))
# ---------------------------------


#  7) Fibonacci Sequence 
# Everyone's favorite Math Problem!

# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation between two adjacent steps in a list
# Create a python function that takes two numbers and finds the next Nine intervals using the Fibonacci Sequence

# ---------------------------------
#      Solution Goes Here ->
def fibonacci(i, j):
    rounds = 1
    arr = [i, j]
    while rounds < 10:
        arr.append(arr[-1] + arr[-2])
        rounds += 1
    return arr
# print(fibonacci(0,1))
# ---------------------------------
