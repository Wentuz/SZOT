def text_to_binary(text):
    binary_string = ' '.join(format(ord(char), '08b') for char in text)
    return binary_string

def binary_to_text(binary):
    binary_chunk = binary.split()
    text = ''.join(chr(int(chunk, 2)) for chunk in binary_chunk)
    return text




if __name__ == '__main__':
    print(text_to_binary("Hello, world!"))
    print(binary_to_text("01001000 01100101 01101100 01101100 01101111 00101100 00100000 01110111 01101111 01110010 01101100 01100100 00100001"))


