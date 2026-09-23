# Task 3: classify values
def classify_number(num):
    if num > 0:
        return "positive"
    if num < 0:
        return "negative"
    return "zero"

#Task 3: generate the first ten prime numbers
def first_ten_primes():
    primes = []
    number = 2

    while len(primes) < 10:
        is_prime = True
        for divisor in range(2, number):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
        number += 1

    return primes

#Task 3: sum numbers from 1 to 100
def sum_to_hundred():
    total = 0
    for number in range(1, 101):
        total += number
    return total


if __name__ == "__main__":
    print(classify_number(0))
    print(first_ten_primes())
    print(sum_to_hundred())

