#encoder/huffman_encoder.py
import collections
import heapq
import os
import time

class Node:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

def calculate_frequencies(input_file):
    with open(input_file, 'r') as file:
        text = file.read()
    text = preprocess_input(text)
    frequency_dict = collections.defaultdict(int)
    for char in text:
        frequency_dict[char] += 1
    return frequency_dict

def build_huffman_tree(frequency_dict):
    priority_queue = []
    for char, frequency in frequency_dict.items():
        node = Node(char, frequency)
        heapq.heappush(priority_queue, node)
    while len(priority_queue) > 1:
        node1 = heapq.heappop(priority_queue)
        node2 = heapq.heappop(priority_queue)
        merged_node = Node(None, node1.frequency + node2.frequency)
        merged_node.left = node1
        merged_node.right = node2
        heapq.heappush(priority_queue, merged_node)
    return priority_queue[0]

def generate_huffman_codes(root, current_code, huffman_codes):
    if root is None:
        return
    if root.char is not None:
        huffman_codes[root.char] = current_code
    generate_huffman_codes(root.left, current_code + '0', huffman_codes)
    generate_huffman_codes(root.right, current_code + '1', huffman_codes)

def get_huffman_codes(root):
    huffman_codes = {}
    generate_huffman_codes(root, '', huffman_codes)
    
    # Special case: If there is only one character, assign it a non-empty code.
    if len(huffman_codes) == 1:
        single_char = list(huffman_codes.keys())[0]
        huffman_codes[single_char] = '0'  # Assign '0' as the code for the single character

    huffman_codes['__EOF__'] = '11111111'
    return huffman_codes



def preprocess_input(text):
    return text.replace('\n', '__NEWLINE__')

def encode_data(input_file, output_file, huffman_codes):
    with open(input_file, 'r') as input_file:
        text = input_file.read()
    text = preprocess_input(text)
    
    # Encoding the text using the Huffman codes
    encoded_data = ''.join(huffman_codes[char] for char in text)
    
    # Padding to ensure the encoded_data length is a multiple of 8
    padding = 8 - (len(encoded_data) % 8)
    padding_info = "{0:08b}".format(padding)  # Store padding info as 8-bit binary
    encoded_data += '0' * padding  # Add padding to the end of the encoded data

    # Convert encoded data to bytes
    with open(output_file, 'wb') as output_file:
        byte_array = bytearray()
        
        # First, write the padding info at the start of the file
        byte_array.append(int(padding_info, 2))
        
        # Then write the encoded data as bytes
        for i in range(0, len(encoded_data), 8):
            byte = encoded_data[i:i + 8]
            byte_array.append(int(byte, 2))
        
        output_file.write(byte_array)

    # Print the encoded data for debugging if necessary
    # print(f"Encoded data: {encoded_data}")

def write_huffman_codes_to_file(huffman_codes, file_path):
    with open(file_path, 'w') as file:
        for char, code in huffman_codes.items():
            file.write(f'{char}:{code}\n')
        file.write(f'__EOF__:{huffman_codes["__EOF__"]}')

def huffman_encode(input_file, output_file, huffman_codes_file):
    start_time = time.time()
    frequency_dict = calculate_frequencies(input_file)
    root = build_huffman_tree(frequency_dict)
    huffman_codes = get_huffman_codes(root)
    write_huffman_codes_to_file(huffman_codes, huffman_codes_file)
    encode_data(input_file, output_file, huffman_codes)
    end_time = time.time()
    execution_time = end_time - start_time
    input_size = os.path.getsize(input_file)
    output_size = os.path.getsize(output_file)
    compression_ratio = input_size / output_size if output_size != 0 else 0
    return execution_time, compression_ratio