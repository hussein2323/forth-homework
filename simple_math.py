def factorial(n):
    if n < 0:
        return "Invalid input"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def is_prime(n):
    if n <= 1:
        return False

    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1

    return True

def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"