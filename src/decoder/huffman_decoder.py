#decoder/huffaman_decoder.py
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

# Step 2: Replace the placeholder with newlines after decoding
def postprocess_output(text):
    return text.replace('__NEWLINE__', '\n')

# Modify your decode_data function to use postprocessing
def huffman_decode(input_file, output_file, huffman_codes):
    with open(input_file, 'r') as input_file:
        encoded_data = input_file.read()

    decoded_data = decode_data(encoded_data, huffman_codes)

    # Postprocess the decoded data (replace __NEWLINE__ with newline)
    decoded_data = postprocess_output(decoded_data)

    with open(output_file, 'w') as output_file:
        output_file.write(decoded_data)


def get_huffman_codes_from_file(huffman_codes_file):
    huffman_codes = {}
    with open(huffman_codes_file, 'r') as file:
        for line in file:
            line = line.strip()
            if line and ':' in line:
                char, code = line.split(':', 1)  # Ensure splitting only at the first occurrence of ':'
                if char == '':  # Special handling for space
                    char = ' '
                huffman_codes[char] = code
    return huffman_codes


def main():
    input_file = os.path.join(os.path.dirname(__file__), '..', '..', 'Data', 'output_file.txt')
    output_file = os.path.join(os.path.dirname(__file__), '..', '..', 'Data', 'decoded_file.txt')
    huffman_codes_file = os.path.join(os.path.dirname(__file__), '..', '..', 'Data', 'huffman_codes.txt')

    huffman_codes = get_huffman_codes_from_file(huffman_codes_file)
    huffman_decode(input_file, output_file, huffman_codes)
