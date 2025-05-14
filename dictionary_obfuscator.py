#!/usr/bin/env python3
import sys
from dictionary_words import dictionary

def process_payload():
    lines = sys.stdin.readlines()

    # Filter out the line containing 'buf' and the line ending with ';'
    content_lines = [
        line.strip()
        for line in lines
        if 'buf' not in line and not line.strip().endswith(';')
    ]

    # Join lines and clean up
    raw_data = ''.join(content_lines).replace('"', '').replace('\\', '').replace(' ', '')

    # Group into byte pairs and format
    bytes_list = [f'"\\x{raw_data[i:i+2]}"' for i in range(0, len(raw_data), 2)]
    result = ','.join(bytes_list)

    return result

payload = process_payload()  
hex_to_index = [ord(hex) for hex in payload]
result = [dictionary[index] for index in hex_to_index]

print(','.join(f'"{item}"' for item in result))
print("\n\n >>>> Size of payload is: ", len(result))

