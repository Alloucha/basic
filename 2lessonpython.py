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
    return name + ' you are ' + str(age*7) + ' years old in dog years'


print(dog_years('Lola', 16))
