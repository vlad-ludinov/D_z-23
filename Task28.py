def sum_number(number1, number2):
    if number1 == 0:
        return number2
    return sum_number(number1 - 1, number2 + 1)
print(sum_number(int(input("Введите одно число: ")), int(input("Введите второе число: "))))
