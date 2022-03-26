import re as _re
import time as _time
import random as _random


"""
Exceptions
"""


class __UnholyWordError(Exception):
    def __str__(self):
        print("An unholy word has been used.")


class __NumberTooBigError(Exception):
    def __str__(self):
        print("I can only convert numbers as big as 9999 :(")


class __WrongAnswerError(Exception):
    def __str__(self):
        print("It's not that hard :(")


class __SelfDestructError(Exception):
    def __str__(self):
        print("BOOOOOOOOOOOOOOOOOMMMMMMMM.")


"""
Util
"""


def __int_to_roman(num):
    """Turns an int into a string containing a roman representation of that
    number.
    """
    roman_numbers = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    normal_numbers = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // roman_numbers[i]):
            roman_num += normal_numbers[i]
            num -= roman_numbers[i]
        i += 1
    return roman_num


"""
The cool stuff :D
"""


def sanctify(text: str) -> str:
    """It turns a given string into a latin-like version.

    The letter "u" is swapped by "v", normal numbers are swapped by roman
    numbers, all letters are capitalized.

    :param text: The string to be formatted
    :type text: str

    :return: The given string, but with capital letters, v instead of u and
    roman numbers instead of normal numbers
    :rtype: str

    :raises TypeError: If a value other than a string is passed as parameter
    :raises UnholyWordError: If the string contains the words: satan, demon,
    baphomet, lucifer, 666 or devil.
    :raises NumberTooBig: If a number is greater than 9999
    """
    if type(text) != str:
        raise TypeError
    sanctified_string = ""
    forbidden_words = ["satan", "demon", "baphomet", "lucifer", "666", "devil"]
    text_format = text.lower()

    # Throws an error if any of the forbidden words are used
    for word in forbidden_words:
        if word in text_format:
            raise __UnholyWordError

    # call the function to swap normal numbers into roman ones, then it swaps
    # those numbers within the string
    numbers_list = _re.findall(r'[0-9]+', text_format)
    numbers_list = sorted(numbers_list, reverse=True, key=len)
    if numbers_list is not None:
        for number in numbers_list:
            num_int = int(number)
            if num_int > 9999:
                raise __NumberTooBigError
            roman_number = __int_to_roman(num_int)
            text_format = text_format.replace(number, roman_number)

    # swaps "u" for "v" because in latin u == v
    for letter in text_format:
        if letter == "u":
            letter = "v"

        # sums up all the characters
        sanctified_string += letter

    # Capital letters because its baseder
    return sanctified_string.upper()


def trinity():
    """
    Explanation of the doctrine of the Holy Trinity through an interactive
    little game
    """
    while True:
        question1 = input(
            "3 variables, father, son and holy_ghost, have the same value: "
            '"God", is it possible to say that they are all "God"?\n'
            "[y] Yes\n"
            "[n] No\n"
        )

        if question1.lower() == "y":
            question2 = input(
                "One value in 3 different variables, one God in 3 different "
                "Persons, simple as.\n"
                "[y] Yes\n"
            )

            if question2.lower() == "y":
                print("🇻🇦")
                break
            else:
                for countdown in range(_random.randint(3, 10), 0, -1):
                    print("Self-destruction in ", countdown)
                    _time.sleep(1)
                raise __SelfDestructError

        elif question1.lower() == "n":
            raise __WrongAnswerError
        else:
            print("Type only y or n")
            _time.sleep(1)
            continue
