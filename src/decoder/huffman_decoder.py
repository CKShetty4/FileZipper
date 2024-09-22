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
    
    for bit in encoded_data:
        temp += bit
        # Check if temp matches any Huffman code
        for char, code in huffman_codes.items():
            if temp == code:
                if char == '__EOF__':
                    return decoded_data  # Stop when EOF is reached
                decoded_data += char
                temp = ''  # Reset temp after a successful match
                break
    return decoded_data


def postprocess_output(text):
    return text.replace('__NEWLINE__', '\n')

def huffman_decode(input_file, output_file, huffman_codes):
    start_time = time.time()
    
    # Read the encoded file as bytes
    with open(input_file, 'rb') as input_file:
        encoded_bytes = input_file.read()

    # The first byte tells us how much padding was added during encoding
    padding = encoded_bytes[0]
    
    # Convert the remaining bytes into a bitstring
    encoded_data = ''.join(format(byte, '08b') for byte in encoded_bytes[1:])
    
    # Remove the padding bits from the end
    if padding > 0:
        encoded_data = encoded_data[:-padding]

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