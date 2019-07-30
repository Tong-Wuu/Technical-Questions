# find the nth fib number using dynamic programming


# Solution 1: Memoization with top down approach
def memoi(n):
    memo = [None] * (n + 1)
    return fib(n, memo)


def fib(i, memo):
    if memo[i] is not None:
        return memo[i]
    if i == 1 or i == 2:
        result = 1
    else:
        result = fib(i - 1, memo) + fib(i - 2, memo)
    # Cache the result in a list based on the nth fib number
    memo[i] = result
    return result


# Solution 2: Bottom up approach
def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    res = [None] * (n + 1)
    res[1] = 1
    res[2] = 1

    for i in range(3, n + 1):
        res[i] = res[i - 1] + res[i - 2]
    return res[n]


print(memoi(100))
print(fib_bottom_up(100))
