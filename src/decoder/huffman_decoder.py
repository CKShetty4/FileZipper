import os
import time

class Node:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

def decode_data(encoded_data, huffman_codes):
    if not encoded_data:
        raise ValueError("Encoded data is empty")
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

def postprocess_output(text):
    return text.replace('__NEWLINE__', '\n')

def huffman_decode(input_file, output_file, huffman_codes):
    start_time = time.time()
    with open(input_file, 'rb') as input_file:
        encoded_bytes = input_file.read()
    encoded_data = ''.join(format(byte, '08b') for byte in encoded_bytes)
    decoded_data = decode_data(encoded_data, huffman_codes)
    decoded_data = postprocess_output(decoded_data)
    with open(output_file, 'w') as output_file:
        output_file.write(decoded_data)
    end_time = time.time()
    execution_time = end_time - start_time
    return decoded_data, execution_time

def get_huffman_codes_from_file(huffman_codes_file):
    huffman_codes = {}
    with open(huffman_codes_file, 'r') as file:
        for line in file:
            line = line.strip()
            if line and ':' in line:
                char, code = line.split(':', 1)
                if char == '':
                    char = ' '
                huffman_codes[char] = code
    return huffman_codes

def main(input_file, output_file, huffman_codes_file):
    huffman_codes = get_huffman_codes_from_file(huffman_codes_file)
    huffman_decode(input_file, output_file, huffman_codes)