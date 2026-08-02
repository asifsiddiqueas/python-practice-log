"""Python program to compress and decompress the string "hello world!helloworld!hello world!hello world!
"""

import zlib

def compress_and_decompress(text):
    
    # encode to bytes and compress
    compressed_data = zlib.compress(text.encode('utf-8'))
    
    # decompress and decode back to string
    decompressed_text = zlib.decompress(compressed_data).decode('utf-8')
    
    return compressed_data, decompressed_text

# test cases
input_data = "hello world!helloworld!hello world!hello world!"

compressed, decompressed = compress_and_decompress(input_data)

print(f"Original text: '{input_data}'")
print(f"Original size: {len(input_data.encode('utf-8'))} bytes")
print(f"Compressed size: {len(compressed)} bytes")
print(f"Decompressed text: '{decompressed}'")
print(f"Data matches exactly: {input_data == decompressed}")