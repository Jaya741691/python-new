# Question 2: Even-Odd List Filter
# Write a function filter_numbers(numbers_list) that takes a list of integers.
# Use a for loop and an if-else statement to separate the even and odd numbers.
# The function should return a tuple containing two lists: (even_numbers, odd_numbers).
from decorator import append


def filter_numbers(numbers_list):
    even_numbers = []
    odd_numbers = []
    for i in numbers_list :
        if i%2==0:
            even_numbers.append(i)
        else:
            odd_numbers.append(i)
    return (even_numbers,odd_numbers)
numbers_list=[21,4,34,5,4,3,23,34,34,53,4,3]
even,odd=filter_numbers(numbers_list)
print("even numbers are : ",even)
print("odd numbers are : ",odd)
