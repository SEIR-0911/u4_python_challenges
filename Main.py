# Python Challenges


#  1) The Time Stone: Lets get cosmic here and begin working with Time.


# - First, lets create a function that converts Minutes to Seconds (1 ->60, 5 -> 300)
def minutues_to_seconds(minutes):
    seconds = minutes * 60
    return seconds

results = minutues_to_seconds(1)
print(results)

results = minutues_to_seconds(5)
print(results)


# -  Then take it up a step further, converting Hours into seconds (1 -> 3600)
def hours_to_seconds(hours):
    seconds = hours * 3600
    return seconds

results = hours_to_seconds(1)
print(results)

results = hours_to_seconds(3.5)
print(results)


# -  We're on the right track here, how many seconds are in a day
def hours_to_seconds(hours):
    seconds = hours * 3600
    return seconds

seconds_in_day = hours_to_seconds(24)
print(seconds_in_day)

# - How many Hours are in the month of June? 
def hours_in_30_days(hours_in_a_day = 24, days = 30):
    total_hours = hours_in_a_day * days
    return total_hours

results = hours_in_30_days()
print(results)


# - How many Minutes are in the month of August?
def mins_in_august(hours_in_day = 24, mins_in_hour = 60, days = 31):
    total_mins = hours_in_day * mins_in_hour * days
    return total_mins

results = mins_in_august()
print(results)



 # Bonus -> Without singing the old showtune in your head, how many Minutes are there in a year? 
 # In days, in weeks, in cups of coffee?


# ---------------------------------
#    Solution Goes Here -> the horses name was Friday
# ---------------------------------



#  2) Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".


# ---------------------------------
def mid(s):
    length = len(s)

    if length % 2 == 0 or length == 0:
        return "no middle letter"
    else:
        middle_index = length // 2
        return s[middle_index]

result1 = mid("abc")
print(result1)

result2 = mid("aaaa")
print(result2)
# ---------------------------------


# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "1234567894444", then it should return "*********4444".


# ---------------------------------
def hide_credit_num(card_number):
    if len(card_number) < 4:
        return "Invalid Card"
    
    hidden_part = '*' * (len(card_number) - 4)
    visible_part = card_number[-4:]

    masked_card_num = hidden_part + visible_part

    return masked_card_num

card_number = "1234449988762222"

result = hide_credit_num(card_number)
print(result)
# ---------------------------------



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
def online_status(statuses):
    online_users = sum(1 for status in statuses.values() if status == 'online')
    return online_users

statuses = {
    "John": "online",
    "Paul": "offline",
    "George": "online",
    "Ringo": "offline"
}

result = online_status(statuses)
print(result)

# ---------------------------------



#  5) Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

# ---------------------------------
def give_discount(full_price, discount_percent):
    if not (0 <= discount_percent <= 100):
        raise ValueError('discount percent should be between 0 and 100')
    discount_amount = (discount_percent / 100) * full_price
    discounted_price = full_price - discount_amount
    return discounted_price

full_price = 100
discount_percent = 20
result = give_discount(full_price, discount_percent)
print(result)
# ---------------------------------


#  6) Pythagorean Theorum

# As any High School sophomore will tell you, the sum of the squares of two legs of a right trangle will equal the square of the hypotenouse.
# Create a function that takes two integers as the Adjacent and Opposite legs of a triangle, and returns an integer of the Hypotenouse


# ---------------------------------
def calculate_hypot(adjacent, opposite):
    hypot = (adjacent**2 + opposite**2)**0.5
    return hypot

adjacent_leg = 3
opposite_leg = 4

result = calculate_hypot(adjacent_leg, opposite_leg)
print(result)

# ---------------------------------


#  7) Fibonacci Sequence 
# Everyone's favorite Math Problem!

# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation between two adjacent steps in a list
# Create a python function that takes two numbers and finds the next Nine intervals using the Fibonacci Sequence

# ---------------------------------
#    
# ---------------------------------
