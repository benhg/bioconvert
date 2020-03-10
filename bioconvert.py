#!/usr/bin/env python3

"""
Convert any biological file format to any other format
"""
import sys
from Bio import SeqIO


def convert(input_file, output_file, in_format, out_format):
    with open(input_file, "rU") as input_handle, open(output_file, "w") as output_handle:
        sequences = SeqIO.parse(input_handle, in_format)
        count = SeqIO.write(sequences, output_handle, out_format) 
    print(f"Converted {count} sequences.")



if __name__ == '__main__':
    
    if len(sys.argv) != 3:
        print("Usage: bioconvert <input file> <input format> <output file> <output format>")
        exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert(input_file, output_file)

