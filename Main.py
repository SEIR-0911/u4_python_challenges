# Python Challenges


#  1) The Time Stone: Lets get cosmic here and begin working with Time.

# - First, lets create a function that converts Minutes to Seconds (1 ->60, 5 -> 300)
def mins_to_seconds(mins):
    seconds_in_min = 60
    seconds_convert = mins * seconds_in_min
    print(seconds_convert)
# mins_to_seconds(4)

# -  Then take it up a step further, converting Hours into seconds (1 -> 3600)
def hours_to_seconds(hour):
    seconds_in_hour = 3600
    seconds_convert = hour * seconds_in_hour
    print(seconds_convert)
# hours_to_seconds(3)

# -  We're on the right track here, how many seconds are in a day
def days_to_seconds():
    seconds_in_hour = 3600
    hours_in_day = 24
    seconds_convert = hours_in_day * seconds_in_hour
    print(seconds_convert)
# days_to_seconds()

# - How many Hours are in the month of June? 
def june_to_hours():
    hours_in_day = 24
    days_in_June = 30
    june_hours = hours_in_day * days_in_June
    print(june_hours)
# june_to_hours()

# - How many Minutes are in the month of August?
 
def mins_in_aug(mins, hrs, days):
    aug_mins = mins * hrs * days
    print(aug_mins)
# mins_in_aug(60, 24, 31)
 
 # Bonus -> Without singing the old showtune in your head, how many Minutes are there in a year? 
def mins_in_year(mins, hrs, days):
    year_mins = mins * hrs * days
    print(year_mins)
# mins_in_year(60, 24, 365)


 # In days, in weeks, in cups of coffee?
def mins_in_day(mins, hrs):
    day_mins = mins * hrs
    print(day_mins)
# mins_in_day(60, 24)

def mins_in_week(mins, hrs, days):
    week_mins = mins * hrs * days
    print(week_mins)
# mins_in_week(60, 24, 7)

# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------



#  2) Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".

def mid(string):
    str_length = len(string)

    if str_length % 2 == 0:
        return""
    else: 
        mid_letter = int((str_length-1) / 2)
        middle_letter= string[mid_letter]
        return(middle_letter)

# print(mid("bart"))


# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "1234567894444", then it should return "*********4444".

def hide_credit_card(card_number):
    hidden_nums = '*' * (len(card_number) - 4) + card_number[-4:]
    print(hidden_nums)
# hide_credit_card("1234567894444")


# ### 4) Online status
# The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

# For example, consider the following dictionary:

# ```
statuses = {
    "John": "online",
    "Paul": "offline",
    "George": "online",
    "Ringo": "online",
    "Ryan": "online"
}

# ```

# In this case, the number of people online is 2.
# Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
# Your function should return the number of people who are online.

# pass if using once
# def online_count():
#     statuses_values = [statuses[key] for key in statuses]
#     print(statuses_values.count("online"))
# online_count()

# Reusable function
def online_count(dictionary):
    dictionary_values = [dictionary[key] for key in dictionary]
    people_online = dictionary_values.count("online")
    return(people_online)

# print(online_count(statuses))



#  5) Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

def total_price(full, disc):
    price = full - (full * disc/100)
    print(price)
# total_price(70, 15)


#  6) Pythagorean Theorum

# As any High School sophomore will tell you, the sum of the squares of two legs of a right trangle will equal the square of the hypotenouse.
# Create a function that takes two integers as the Adjacent and Opposite legs of a triangle, and returns an integer of the Hypotenouse

def hypotenuse(a, b):
    c_squared = a**2 + b**2
    c = c_squared**0.5
    print(c)
# hypotenuse(7, 10)


# import math for math.sqrt

# def hypotenuse(a, b):
#     hypot = math.sqrt(a**2 + b**2)
# print(hypotenuse(7, 10))



#  7) Fibonacci Sequence 
# Everyone's favorite Math Problem!

# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation between two adjacent steps in a list
# Create a python function that takes two numbers and finds the next Nine intervals using the Fibonacci Sequence

def fibonacci(num1, num2, count):
    num_list = [num1, num2]
    for x in range(count):
        num_list.append(num_list[-1] + num_list[-2])
    return num_list
print(fibonacci(2, 3, 9))
