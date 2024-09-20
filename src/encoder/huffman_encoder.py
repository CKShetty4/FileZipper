
#encoder/huffaman_encoder.py
#Step 1.1: Read the input file and calculate the frequency of each character
import collections 

# Step 1.2: Build a Huffman tree based on the character frequencies
import heapq

#1.5
import os

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
def encode_data(input_file, output_file, huffman_codes):
    with open(input_file, 'r') as input_file:
        text = input_file.read()

    encoded_data = ''
    for char in text:
        encoded_data += huffman_codes[char]

    with open(output_file, 'w') as output_file:
        output_file.write(encoded_data)

#Step 1.5: Write the huffman codes to file
def write_huffman_codes_to_file(huffman_codes):
    # Get the absolute path of the file
    file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'Data', 'huffman_codes.txt')
    with open(file_path, 'w') as file:
        for char, code in huffman_codes.items():
            file.write(f'{char}:{code}\n')

# Step 1.4: Write the encoded data to the output file
def huffman_encode(input_file, output_file):
    frequency_dict = calculate_frequencies(input_file)
    root = build_huffman_tree(frequency_dict)
    huffman_codes = get_huffman_codes(root)
    write_huffman_codes_to_file(huffman_codes)#Step 1.5: Write the huffman codes to file
    encode_data(input_file, output_file, huffman_codes)
    

