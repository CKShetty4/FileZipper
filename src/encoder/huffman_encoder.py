import collections
import heapq

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
    return huffman_codes

def encode_data(input_file, output_file, huffman_codes):
    with open(input_file, 'r') as input_file:
        text = input_file.read()

    encoded_data = ''
    for char in text:
        encoded_data += huffman_codes[char]

    with open(output_file, 'w') as output_file:
        output_file.write(encoded_data)

def huffman_encode(input_file, output_file):
    frequency_dict = calculate_frequencies(input_file)
    root = build_huffman_tree(frequency_dict)
    huffman_codes = get_huffman_codes(root)
    encode_data(input_file, output_file, huffman_codes)

# Example usage:
huffman_encode('../../Data/input_file.txt', '../../Data/output_file.txt')