# 1) The Time Stone

# Function to convert minutes to seconds
def minutes_to_seconds(minutes):
    return minutes * 60

# Function to convert hours to seconds
def hours_to_seconds(hours):
    return hours * 3600

# Number of seconds in a day
seconds_in_a_day = hours_to_seconds(24)

# Number of hours in the month of June (assuming 30 days in June)
hours_in_june = 30 * 24

# Number of minutes in the month of August (assuming 31 days in August)
minutes_in_august = 31 * 24 * 60

# Bonus: Number of minutes in a year
minutes_in_a_year = 365 * 24 * 60
days_in_a_year = 365
weeks_in_a_year = days_in_a_year / 7
cups_of_coffee_in_a_year = days_in_a_year * 3  # Assuming 3 cups of coffee per day

# 2) Middle letter

def mid(s):
    length = len(s)
    if length % 2 == 0:
        return ""
    else:
        middle_index = length // 2
        return s[middle_index]

# 3) Hide the credit card number

def hide_credit_card(card_number):
    hidden_part = '*' * (len(card_number) - 4)
    return hidden_part + card_number[-4:]

# 4) Online status

def online_count(statuses):
    return list(statuses.values()).count("online")

# 5) Give me the discount

def apply_discount(full_price, discount_percentage):
    discounted_price = full_price - (full_price * discount_percentage / 100)
    return discounted_price

# 6) Pythagorean Theorem

def calculate_hypotenuse(adjacent, opposite):
    hypotenuse = (adjacent**2 + opposite**2)**0.5
    return hypotenuse

# 7) Fibonacci Sequence

def fibonacci_sequence(num1, num2, intervals):
    sequence = [num1, num2]
    for _ in range(intervals - 2):
        next_num = num1 + num2
        sequence.append(next_num)
        num1, num2 = num2, next_num
    return sequence

# Testing the functions
print(minutes_to_seconds(5))
print(hours_to_seconds(1))
print(seconds_in_a_day)
print(hours_in_june)
print(minutes_in_august)
print(minutes_in_a_year, days_in_a_year, weeks_in_a_year, cups_of_coffee_in_a_year)
print(mid("abc"))
print(mid("aaaa"))
print(hide_credit_card("1234567894444"))
print(online_count({"John": "online", "Paul": "offline", "George": "online", "Ringo": "offline"}))
print(apply_discount(100, 20))
print(calculate_hypotenuse(3, 4))
print(fibonacci_sequence(0, 1, 9))
