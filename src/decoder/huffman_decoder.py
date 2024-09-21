#decoder/huffman_decoder.py
import os
import time

class Node:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

def decode_data(encoded_data, huffman_codes):
    decoded_data = ''
    temp = ''
    for i in range(0, len(encoded_data), 8):
        byte = encoded_data[i:i+8]
        temp += byte
        while True:
            for char, code in huffman_codes.items():
                if temp.startswith(code):
                    if char == '__EOF__':
                        temp = temp[len(code):]  # Remove the EOF code
                        return decoded_data  # Stop decoding when EOF is reached
                    decoded_data += char
                    temp = temp[len(code):]
                    break
            else:
                break
    return decoded_data

def postprocess_output(text):
    return text.replace('__NEWLINE__', '\n')

def huffman_decode(input_file, output_file, huffman_codes):
    start_time = time.time()
    with open(input_file, 'rb') as input_file:
        encoded_bytes = input_file.read()
    encoded_data = ''.join(format(byte, '08b') for byte in encoded_bytes)
    # Remove padding bytes
    padding = 8 - (len(encoded_data) % 8)
    encoded_data = encoded_data[:-padding]
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
    # huffman_codes['END'] = '11111111'
    # print("Huffman codes:", huffman_codes)  # Add this line to verify the dictionary
    return huffman_codes

def main(input_file, output_file, huffman_codes_file):
    huffman_codes = get_huffman_codes_from_file(huffman_codes_file)
    huffman_decode(input_file, output_file, huffman_codes)