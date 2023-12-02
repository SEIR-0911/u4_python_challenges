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
secs_in_min = 60
mins_in_hour = 60
hours_in_day = 24
days_in_week = 7
days_in_year = 365
days_in_June = 30
days_in_August = 31

def convert_mins_to_secs(min):
    min_in_secs = min * secs_in_min
    return(min_in_secs)

#print(convert_mins_to_secs(1))

def convert_hrs_to_secs(hours):
    hours_in_secs = hours * mins_in_hour * secs_in_min
    return(hours_in_secs)

#print(convert_hrs_to_secs(1))

def convert_days_to_secs(num_of_days):
    days = num_of_days
    days_in_secs = days * hours_in_day * mins_in_hour * secs_in_min
    return(days_in_secs)

#print(convert_days_to_secs(1))

def hrs_in_June():
    return (days_in_June * hours_in_day)

#print(hrs_in_June())

def mins_in_Aug():
    return(days_in_August * hours_in_day * mins_in_hour)

#print(mins_in_Aug())

def mins_in_year(num_of_yrs):
    return(num_of_yrs * days_in_year * hours_in_day * mins_in_hour)

#print(mins_in_year(1))

def mins_in_days(days):
    return(days * hours_in_day * mins_in_hour)

#print(mins_in_days(5))

def mins_in_weeks(weeks):
    no_weeks=weeks
    return (no_weeks * days_in_week * hours_in_day * mins_in_hour)

#print(mins_in_weeks(1))


#  2) Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------
def mid(str):
    if len(str) % 2 == 0:
        return 'no middle'
    else:
        i = len(str) // 2
        return str[i]

# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "1234567894444", then it should return "*********4444".


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------
def hide_numbers(nums):
    return '*' * (len(nums)-4) + nums[-4:]


# ### 4) Online status
# The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

# For example, consider the following dictionary:

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
def online_count(dictionary):
    dictionary_values = [dictionary[key] for key in dictionary]
    people_online = dictionary_values.count("online")
    return(people_online)


#  5) Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------
def get_sale_price(full_price, discount_pct):
    sale_price = int(full_price * ((100-discount_pct)/100))
    return sale_price

#  6) Pythagorean Theorum

# As any High School sophomore will tell you, the sum of the squares of two legs of a right trangle will equal the square of the hypotenouse.
# Create a function that takes two integers as the Adjacent and Opposite legs of a triangle, and returns an integer of the Hypotenouse


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------
def pythagorean(a, b):
    return ((a ** 2) + (b ** 2)) ** .5

#  7) Fibonacci Sequence 
# Everyone's favorite Math Problem!

# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation between two adjacent steps in a list
# Create a python function that takes two numbers and finds the next Nine intervals using the Fibonacci Sequence
def fibonacci(i, j):
    rounds = 1
    arr = [i, j]
    while rounds < 10:
        arr.append(arr[-1] + arr[-2])
        rounds += 1
    return arr
# print(fibonacci(0,1))
# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------
