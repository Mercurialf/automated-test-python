import random
import string
from random import randint


class Utils:
    @staticmethod
    def generate_random_string():
        letters = string.ascii_letters
        rand_string = ''.join(random.choice(letters) for i in range(10))
        return rand_string

    @staticmethod
    def string_comparisons(original_string, get_string):
        if original_string == get_string:
            return True

    @staticmethod
    def random_number():
        return randint(0, 100)
