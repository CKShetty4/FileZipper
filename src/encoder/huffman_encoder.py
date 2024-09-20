#encoder/huffaman_encoder.py
#Step 1.1: Read the input file and calculate the frequency of each character
import collections 
# Step 1.2: Build a Huffman tree based on the character frequencies
import heapq
#1.5
import os
#1.6
import time


class Node:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency
#Step 1.1: Read the input file and calculate the frequency of each character
def calculate_frequencies(input_file):
    with open(input_file, 'r') as file:
        text = file.read()

    # Preprocess the text (replace newline with __NEWLINE__)
    text = preprocess_input(text)

    frequency_dict = collections.defaultdict(int)
    for char in text:
        frequency_dict[char] += 1

    return frequency_dict

# Step 1.2: Build a Huffman tree based on the character frequencies
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
# Step 1.3: Traverse the Huffman tree to generate the Huffman codes for each character
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
    return huffman_codes

# Step 1.4: Write the encoded data to the output file
# Step 1: Replace newlines with a unique placeholder before encoding
def preprocess_input(text):
    return text.replace('\n', '__NEWLINE__')

# Modify your encode_data function to use preprocessing
def encode_data(input_file, output_file, huffman_codes):
    with open(input_file, 'r') as input_file:
        text = input_file.read()

    # Preprocess the text (replace newline with __NEWLINE__)
    text = preprocess_input(text)

    encoded_data = ''
    for char in text:
        encoded_data += huffman_codes[char]

    # Write as binary
    with open(output_file, 'wb') as output_file:  # 'wb' for binary write mode
        byte_array = bytearray()
        for i in range(0, len(encoded_data), 8):
            byte = encoded_data[i:i + 8]  # Take 8 bits at a time
            byte_array.append(int(byte, 2))  # Convert string to binary and append
        output_file.write(byte_array)




#Step 1.5: Write the huffman codes to file
def write_huffman_codes_to_file(huffman_codes,file_path):
    # Get the absolute path of the file
    with open(file_path, 'w') as file:
        for char, code in huffman_codes.items():
            file.write(f'{char}:{code}\n')

# Step 1.4: Write the encoded data to the output file
def huffman_encode(input_file, output_file,huffman_codes_file):
    start_time = time.time()
    frequency_dict = calculate_frequencies(input_file)
    root = build_huffman_tree(frequency_dict)
    huffman_codes = get_huffman_codes(root)
    write_huffman_codes_to_file(huffman_codes,huffman_codes_file)#Step 1.5: Write the huffman codes to file
    encode_data(input_file, output_file, huffman_codes)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f'Execution time: {execution_time:.2f} seconds')

    # Calculate compression ratio
    input_size = os.path.getsize(input_file)
    output_size = os.path.getsize(output_file)
    compression_ratio = input_size / output_size if output_size != 0 else 0
    # print(f'File is compressed {compression_ratio:.2f} times of it\'s orginal size')
    return execution_time, compression_ratio
    