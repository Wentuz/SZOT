from random import randint


def generate_number() -> int:
    return randint(0,100)


if __name__ == '__main__':
    print(generate_number())