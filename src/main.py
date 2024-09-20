# main.py
import os
from encoder.huffman_encoder import huffman_encode
from decoder.huffman_decoder import main as huffman_decode_main


def main():
    input_file = os.path.join(os.path.dirname(__file__), '..', 'Data', 'input_file.txt')
    output_file = os.path.join(os.path.dirname(__file__), '..', 'Data', 'output_file.txt')
    decoded_file = os.path.join(os.path.dirname(__file__), '..', 'Data', 'decoded_file.txt')
    huffman_codes_file = os.path.join(os.path.dirname(__file__), '..', 'Data', 'huffman_codes.txt')
    
    huffman_encode(input_file, output_file,huffman_codes_file)
    huffman_decode_main(output_file, decoded_file, huffman_codes_file)

if __name__ == '__main__':
    main()