#main.py
import os
from encoder.huffman_encoder import huffman_encode
from decoder.huffman_decoder import main as huffman_decode_main


def main():
    input_file = os.path.join(os.path.dirname(__file__), '..', 'Data', 'input_file.txt')
    output_file = os.path.join(os.path.dirname(__file__), '..', 'Data', 'output_file.txt')
    
    huffman_encode(input_file, output_file)
    huffman_decode_main()

if __name__ == '__main__':
    main()