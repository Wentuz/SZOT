
def read_WH(user_input: str) -> str:

    path = 'WHfiles/' + user_input[4:] + '.txt'
    file = open(path, 'r')
    lines = file.readlines()
    return lines

if __name__ == '__main__':
    read_WH("!wh weapons")