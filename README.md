# Greedy Huffman Encoder - File Zipper

## Project Overview

The **File Zipper** project is a file compression utility that utilizes the Greedy Huffman encoding algorithm to efficiently compress files. This project demonstrates the practical use of a greedy algorithm, allowing users to reduce the size of large files while maintaining the original content.

The focus of this project is to provide a balance between compression ratio and execution time, helping users understand how Huffman encoding optimizes file sizes without compromising on speed.

## Features

- **File Compression**: Compress large files using Huffman encoding.
- **File Decompression**: Restore compressed files to their original form.
- **Greedy Algorithm Application**: Learn how the greedy algorithm is applied in file compression.
- **Compression Ratio vs Execution Time**: Analyze the trade-offs between file size reduction and the time required for compression.

## How It Works

Huffman encoding is a lossless compression method that assigns variable-length codes to characters based on their frequency. Frequently occurring characters are given shorter codes, while less common characters receive longer ones, minimizing the overall file size.

1. **Frequency Calculation**: The frequency of each character in the file is calculated.
2. **Building the Huffman Tree**: A binary tree is constructed, where the least frequent characters are placed deeper in the tree and the most frequent characters are closer to the root.
3. **Assigning Codes**: Shorter binary codes are assigned to frequent characters, and longer codes to infrequent characters.
4. **Encoding the File**: The file is encoded using these binary codes.
5. **Decompression**: The encoded file can be decompressed by reversing the Huffman tree process.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/CKShetty4/FileZipper.git
   ```

2. Navigate to the project directory:

   ```bash
   cd FileZipper
   ```

## Running the Program

### To Compress a File:

You can compress a file by:

1. **Navigating to the `encoder` folder**, adding your input file, and running:
   ```bash
   python huffman_encoder.py compress <input_file.txt>
   ```

2. **Or adding the input file to the `Data` folder**, navigating to the `src` folder, and running:
   ```bash
   python -B main.py compress <input_file.txt> <output_file.txt>
   ```
   > *The `-B` flag is used to prevent the generation of Python cache files.*

   The compressed output file will be saved in the same directory as the input file.

### To Decompress a File:

You can decompress a file by:

1. **Navigating to the `decoder` folder**, adding your compressed file, and running:
   ```bash
   python huffman_decoder.py decompress <compressed_file.txt> <huffman_codes_file.txt>
   ```

2. **Or navigating to the `src` folder** and running:
   ```bash
   python -B main.py decompress <compressed_file.txt> <decoded_file.txt>
   ```

### Example

```bash
python huffman_encoder.py compress example.txt
python huffman_decoder.py decompress compressed.txt
```

> You can also run both encoding and decoding together (for testing purposes, as the input and output files will be identical) by using:
```bash
python -B main.py
```

### Testing

To run the automated test cases, navigate to the `src` folder and run:

```bash
python -B test_huffman.py
```

This will execute 12 test cases, display the results in the terminal, and generate a `testResultlog.txt` file with the test results.

## Example Files

- **input_file.txt**: A sample input file to demonstrate compression.
- **output_file.txt**: The output file generated after applying Huffman compression.
- **decoded_file.txt**: The file generated after decompression, which should match the original input.

## File Structure

```
FileZipper/
├── Data/
├── src/
│   ├── encoder/
│   │   └── huffman_encoder.py
│   ├── decoder/
│   │   └── huffman_decoder.py
│   └── main.py
│   ├── test_huffman.py
```

## Compression Ratio and Execution Time

One of the core aspects of this project is to explore the trade-off between compression ratio and execution time:

- **Compression Ratio**: Huffman encoding can significantly reduce file size, particularly for files with many repeated characters.
- **Execution Time**: While the algorithm is efficient, compression and decompression times increase with larger files and more complex character distributions.

## Future Improvements

- Add support for compressing multiple input files into a single compressed file.
- Implement functionality to decompress a single compressed file back into multiple files.
