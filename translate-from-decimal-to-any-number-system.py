def translate(number, base=2):
    if number == 0:
        return "0"
    
    digits = []
    while number > 0:
        digits.append(str(number % base))
        number //= base
    return ''.join(digits[::-1])
