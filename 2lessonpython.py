def tenth_power(num):
    return num ** 10


print(tenth_power(1))
print(tenth_power(0))
print(tenth_power(2))


def first_three_multiples(num):
    print(num * 1)
    print(num * 2)
    print(num * 3)
    return num * 3


first_three_multiples(10)
first_three_multiples(0)


def tip(total, percentage):
    return total * (percentage / 100)


print(tip(10, 25))
print(tip(0, 100))


def introduction(first_name, last_name):
    return last_name + ', ' + first_name + ' ' + last_name


print(introduction('James', 'Bond'))


def dog_years(name, age):
    return name + ' you are ' + str(age * 7) + ' years old in dog years'


print(dog_years('Lola', 16))


def large_power(base, exponent):
    if base ** exponent > 5000:
        return True
    else:
        return False


print(large_power(2, 14))


def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
    if budget < (food_bill + electricity_bill + internet_bill + rent):
        return True
    else:
        return False


print(over_budget(100, 20, 30, 10, 40))


def twice_as_large(num1, num2):
    if num1 > num2 * 2:
        return True
    else:
        return False


print(twice_as_large(10, 5))


def divisible_by_ten(num):
    if num % 10:
        return False
    else:
        return True


print(divisible_by_ten(20))


def not_sum_to_ten(num1, num2):
    if num1 + num2 != 10:
        return True

    else:
        return False


print(not_sum_to_ten(9, -1))
print(not_sum_to_ten(9, 1))


def in_range(num, lower, upper):
    if lower <= num <= upper:
        return True
    else:
        return False


print(in_range(10, 10, 10))
print(in_range(5, 10, 20))


def same_name(your_name, my_name):
    if your_name == my_name:
        return True
    else:
        return False


print(same_name("Colby", "Colby"))
print(same_name("Tina", "Amber"))


def always_false(num):
    if num >= 0 and num <= 0:
        return False
    else:
        return False


print(always_false(0))
print(always_false(-1))
print(always_false(1))


def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3
    else:
        return "It's a tie!"

print(max_num(-10, 0, 10))
print(max_num(-10, 5, -30))
print(max_num(-5, -10, -10))
print(max_num(2, 3, 3))