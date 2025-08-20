def dfactorial(n):
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(n % 2 or 2, n + 1, 2):
        result *= i
    return result
