def mult(number, degree):
    if degree == 1:
        return number
    return number * mult(number, degree-1)
print(mult(int(input("Введите число: ")), int(input("Введите степень: "))))
