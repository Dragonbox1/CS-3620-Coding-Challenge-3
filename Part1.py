def student_discount(price):
    return price - (price / 10)


def regular_discount(price):
    return price - (price / 20)


defaultPrice = 500.00
studentPrice = student_discount(defaultPrice)
regStudentPrice = regular_discount(studentPrice)
print(regStudentPrice)