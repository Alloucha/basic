"""Write a function named count_char_x that takes a string named word and a single character named x as parameters.
The function should return the number of times x appears in word."""


def count_char_x(word, x):
    count = 0
    for char in word:
        if x == char:
            count += 1
    return count


print(count_char_x("mississippi", "s"))
print(count_char_x("mississippi", "m"))

""" Write a function named count_multi_char_x that takes a string named word and a string named x. 
This function should do the same thing as the count_char_x function you just wrote - 
it should return the number of times x appears in word. 
However, this time, make sure your function works when x is multiple characters long.
For example, count_multi_char_x("Mississippi", "iss") should return 2"""


def count_multi_char_x(word, x):
    count = 0
    for char in word.split(x):
        count += 1
    return count - 1


print(count_multi_char_x("mississippi", "iss"))
print(count_multi_char_x("apple", "pp"))

""" Write a function called check_for_name that takes two strings as parameters named sentence and name. The function should return True if name appears in sentence in all lowercase letters, all uppercase letters, or with any mix of uppercase and lowercase letters. The function should return False otherwise.
For example, the following three calls should all return True:"""


def check_for_name(sentence, name):
    if name.lower() in sentence.lower():
        return True
    elif name.upper() in sentence.upper():
        return True
    else:
        return False


print(check_for_name("My name is Jamie", "Jamie"))
print(check_for_name("My name is jamie", "Jamie"))
print(check_for_name("My name is Samantha", "Jamie"))


""" Create a function called x_length_words that takes a string named sentence and an integer named x as parameters. 
This function should return True if every word in sentence has a length greater than or equal to x."""
def x_length_words(sentence, x):
    sentence = sentence.split(' ')
    for item in sentence:
        if len(item) >= x:
            return True
        else:
            return False


print(x_length_words("i like apples", 2))
print(x_length_words("he likes apples", 2))
