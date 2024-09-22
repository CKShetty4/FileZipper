# Greedy Huffman Encoder - File Zipper

## Project Overview

The **File Zipper** project is a file compression utility that leverages the Greedy Huffman encoding algorithm to efficiently compress files. By implementing this compression technique, the project demonstrates a practical application of a **greedy algorithm**, which allows users to compress large files into smaller ones while maintaining the original information.

The focus of this project is to provide an understanding of the trade-offs between **compression ratio** and **execution time**—helping users see how Huffman encoding optimizes file sizes and the speed of compression.

## Features

- **File Compression**: Compress large files using Huffman encoding.
- **File Decompression**: Restore compressed files back to their original state.
- **Greedy Algorithm Application**: Understand how the greedy approach works in the context of file compression.
- **Compression Ratio vs Execution Time**: Analyze the balance between compression efficiency and the time taken for compression.

## How It Works

Huffman encoding is a **lossless compression** technique that uses a frequency-based binary tree to assign variable-length codes to characters. Characters that occur more frequently are given shorter codes, while less frequent ones are given longer codes, reducing the overall file size.

1. **Frequency Calculation**: The algorithm starts by calculating the frequency of each character in the file.
2. **Building the Huffman Tree**: A binary tree is constructed where the lowest frequency characters are placed at deeper levels, and higher frequency characters are closer to the root.
3. **Assigning Codes**: The algorithm assigns shorter binary codes to more frequent characters and longer codes to infrequent characters.
4. **Encoding the File**: The file is then encoded using the generated binary codes.
5. **Decompression**: The encoded file can be decompressed back to its original state by reversing the Huffman tree process.

## Usage



### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/CKShetty4/FileZipper.git
   ```

2. Navigate to the project directory:
   ```bash
   cd FileZipper
   ```

### Running the Program (Still need be implemented though)
To compress a file:
```bash
python huffman_encoder.py compress <input_file> <output_file>
```
To decompress a file:
```bash
python huffman_encoder.py decompress <compressed_file> <output_file>
```
Example:
```bash 
python huffman_encoder.py compress example.txt
python huffman_encoder.py decompress decompressed.txt
```
#### Example Files
- **input_file.txt**: A sample input file to demonstrate compression.
- **output_file.txt**: The output after applying Huffman compression.
- **decoded_file.txt**: The file after decompression, which matches the original input.

### File Structure
```bash\
FileZipper/
├── src/
│   ├── encoder/
│   │   └── huffman_encoder.py
│   ├── decoder/
│   │   └── huffman_decoder.py
│   └── main.py
│   ├── test_huffman.py
```
### Compression Ratio and Time Trade-Offs
One of the core aspects of this project is to illustrate the trade-off between `compression ratio` and `execution time`:

**Compression Ratio**: Huffman encoding can achieve significant file size reductions, especially for files with many repeated characters.
**Execution Time**: Although the algorithm is efficient, compression and decompression times increase with larger files and more complex character distributions.
