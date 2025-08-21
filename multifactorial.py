def Kfactorial(n, k=1):
    if n <= 0:
        return 1
    if n <= k:
        return n
    return n * Kfactorial(n - k, k)
