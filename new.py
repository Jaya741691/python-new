# Question 3: The FizzBuzz UpgradedWrite a function fizzbuzz_dict(n) that accepts an integer $n$. It should iterate from
# 1 to $n$ and build a dictionary where:The key is the number.The value is "Fizz" if divisible by 3, "Buzz" if divisible
# by 5, "FizzBuzz"
# if divisible by both, and the number itself as a string if divisible by neither.Constraint:
# If the number is a multiple of 7, skip adding it to the dictionary entirely using continue.


def fizzbuzz_dict(n):
    result_dict = {}

    for i in range(1, n + 1):
        if i % 7 == 0:
            continue

        if i % 3 == 0 and i % 5 == 0:
            result_dict[i] = "FizzBuzz"
        elif i % 3 == 0:
            result_dict[i] = "Fizz"
        elif i % 5 == 0:
            result_dict[i] = "Buzz"
        else:
            result_dict[i] = str(i)

    return result_dict

print(fizzbuzz_dict(15))


