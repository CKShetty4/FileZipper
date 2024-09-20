import os

class Node:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

def decode_data(encoded_data, huffman_codes):
    decoded_data = ''
    temp = ''
    for bit in encoded_data:
        temp += bit
        for char, code in huffman_codes.items():
            if temp == code:
                decoded_data += char
                temp = ''
                break
    return decoded_data

def huffman_decode(input_file, output_file, huffman_codes):
    with open(input_file, 'r') as input_file:
        encoded_data = input_file.read()

    decoded_data = decode_data(encoded_data, huffman_codes)

    with open(output_file, 'w') as output_file:
        output_file.write(decoded_data)

def get_huffman_codes_from_file(file_path):
    with open(file_path, 'r') as file:
        huffman_codes = {}
        for line in file:
            char, code = line.strip().split(':')
            huffman_codes[char] = code
        return huffman_codes

def main():
    input_file = '../../Data/output_file.txt'
    output_file = '../../Data/decoded_file.txt'
    huffman_codes_file = '../../Data/huffman_codes.txt'

    huffman_codes = get_huffman_codes_from_file(huffman_codes_file)
    huffman_decode(input_file, output_file, huffman_codes)

if __name__ == '__main__':
    main()