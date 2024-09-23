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
    
    # Create a reverse lookup for huffman codes (bit sequences as keys)
    reverse_huffman_codes = {code: char for char, code in huffman_codes.items()}
    
    for bit in encoded_data:
        temp += bit
        
        # Check if temp matches any Huffman code
        if temp in reverse_huffman_codes:
            char = reverse_huffman_codes[temp]
            
            if char == '__EOF__':
                break  # Stop decoding when EOF is reached
            
            decoded_data += char
            temp = ''  # Reset temp after a successful match
    
    return decoded_data


import re

def postprocess_output(text):
    special_chars = [
        ('@', '__SPECIAL_AT'),
        ('#', '__SPECIAL_HASH'),
        ('$','__SPECIAL_DOLLAR'),
        ('%', '__SPECIAL_PERCENT'),
        ('^', '__SPECIAL_CARET'),
        ('&', '__SPECIAL_AND'),
        ('*', '__SPECIAL_STAR'),
        ('(', '__SPECIAL_LEFT_PAREN'),
        (')', '__SPECIAL_RIGHT_PAREN'),
        ('_', '__SPECIAL_UNDERSCORE'),
        ('+', '__SPECIAL_PLUS'),
        ('{', '__SPECIAL_LEFT_BRACE'),
        ('}', '__SPECIAL_RIGHT_BRACE'),
        ('|', '__SPECIAL_VERTICAL_BAR'),
        (':', '__SPECIAL_COLON'),
        ('<', '__SPECIAL_LEFT_ANGLE_BRACKET'),
        ('>', '__SPECIAL_RIGHT_ANGLE_BRACKET'),
    ]
    for char, special_char in special_chars:
        text = text.replace(special_char, char)
    return text.replace('__NEWLINE__', '\n')

def huffman_decode(input_file, output_file, huffman_codes):
    start_time = time.time()
    
    # Read the encoded file as bytes
    with open(input_file, 'rb') as input_file:
        encoded_bytes = input_file.read()

    # The first byte tells us how much padding was added during encoding
    padding = encoded_bytes[0]
    print(f"Padding in the file: {padding}")

    # Convert the remaining bytes into a bitstring
    encoded_data = ''.join(format(byte, '08b') for byte in encoded_bytes[1:])
    
    print(f"Encoded data before removing padding: {encoded_data}")
    
    # Remove the padding bits from the end
    if padding > 0:
        encoded_data = encoded_data[:-padding]

    print(f"Encoded data after removing padding: {encoded_data}")

    # Decode the data using the Huffman codes
    decoded_data = decode_data(encoded_data, huffman_codes)
    
    # Post-process the decoded data to handle newlines, etc.
    decoded_data = postprocess_output(decoded_data)
    
    # Write the decoded data to the output file
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
    huffman_codes['__EOF__'] = '11111111'
    # print("Huffman codes:", huffman_codes)  # Add this line to verify the dictionary
    return huffman_codes

def main(input_file, output_file, huffman_codes_file):
    huffman_codes = get_huffman_codes_from_file(huffman_codes_file)
    huffman_decode(input_file, output_file, huffman_codes)