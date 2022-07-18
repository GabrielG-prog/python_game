import random

class Utils:

    @staticmethod
    def read_number(msg, min, max):
        while True:
            try:
                res = int(input(msg))
                if res > max or res < min:
                    print(f"Please enter a value between {min} and {max}")

                return res
            except ValueError:
                print("Please a numerical value !")


    def random_number(self, val1, val2):
        random.randint(val1, val2)