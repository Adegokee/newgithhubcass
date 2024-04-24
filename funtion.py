

# Function to calculate the average of a list of numbers
# def calculate_average(numbers):
#     return sum(numbers) / len(numbers) if numbers else 0
# print(calculate_average([30, 50, 200]))  

# # Function to check if a number is prime
# def is_prime(number):
#     if number < 2:
#         return False
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False
#     return True
# print(is_prime(2))

# # Function to reverse a string
# def reverse_string(s):
#     return s[::-1]
# print(reverse_string())

# Function to calculate factorial of a number
# def factorial(t):
#     if t == 0:
#         return 1
#     else:
#         return t * factorial(t-1)
# print(factorial(5))

# # Function to count vowels in a string
# def count_vowels(s):
#     write = 'aeiouAEIOU'
#     count = 0
#     for x in s:
#         if x in write:
#             count += 1
#     return count
# print(count_vowels('tundea'))

# # Function to check if a string is palindrome
# def check_palindrome(s):
#     return s == s[::-1]


# # Function to find maximum value in a list
# def find_max(numbers):
#     return max(numbers) if numbers else None

# # Function to calculate power
# def calculate_power(base, exponent):
#     return base ** exponent
# print(calculate_power(2, 2))

# # Function to remove duplicates from a list while preserving order
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
print(remove_duplicates("Adegoke"))