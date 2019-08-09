# Given a integer find sum of all the prime within that range


# 1) a prime number is a number that is only divisible by itself and one.
# 2) numbers that have more than two factors are called composite numbers
# 3) for each number going up to n check whether it is a prime or not
# 4) added to variable if it is
def sumOfPrime(n):
    res = 0
    for num in range(2, n + 1):
        if isPrime2(num):
            res += num

    return res


def isPrime(x):
    factors = 0
    for i in range(1, x + 1):
        if (x % i) == 0:
            factors += 1

    if factors == 2:
        return True

    return False


def isPrime2(y):
    import math
    i = 2
    while i <= math.sqrt(y):
        if (y % i) == 0:
            return False
        i += 1

    return True


print(sumOfPrime(1000))
