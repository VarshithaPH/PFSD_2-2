import random
import string

def generate_random_color():
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return color

def generate_random_string(length=5):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def generate_random_number_between(minimum, maximum):
    return random.randint(minimum, maximum)

def generate_random_multiple_of_seven():
    return random.randint(0, 10) * 7

if __name__ == "__main__":
    random_color = generate_random_color()
    random_string = generate_random_string()
    random_number = generate_random_number_between(1, 100)
    random_multiple_of_seven = generate_random_multiple_of_seven()

    print("Random Color Hex:", random_color)
    print("Random Alphabetical String:", random_string)
    print("Random Number between 1 and 100:", random_number)
    print("Random Multiple of 7 between 0 and 70:", random_multiple_of_seven)
