def revereseInt(number):
    result = 0
    while number != 0:
        reminder = int(number % 10)
        result = result * 10 + reminder
        number = int(number / 10)
    return result

print(revereseInt(1234))
print(revereseInt(8762))