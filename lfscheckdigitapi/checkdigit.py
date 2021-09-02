def calculateCheckDigit(number):
    checkDigit = 0
    sum = 0
    i = 0

    for digit in map(int, number):
        i += 1
        if i % 2 == 0:
            sum += digit
        else:
            sum += digit * 3

    checkDigit = 10 - sum % 10

    return checkDigit