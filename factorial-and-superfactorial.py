def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def sf(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= factorial(i)
    return result
