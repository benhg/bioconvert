#!/usr/bin/env python3

"""
Convert any biological file format to any other format
"""
import argparse
from Bio import SeqIO


def convert(input_file, in_format, output_file, out_format):
    with open(input_file, "rU") as input_handle, open(output_file, "w") as output_handle:
        sequences = SeqIO.parse(input_handle, in_format)
        count = SeqIO.write(sequences, output_handle, out_format) 
    print(f"Converted {count} sequences.")



if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Convert bioinformatic files')

    parser.add_argument('--input', type=str, help='input file for conversion')
    parser.add_argument('--infmt', type=str, help='input file format')
    parser.add_argument('--output', type=str, help='output file for conversion')
    parser.add_argument('--outfmt', type=str, help='output file format')
    args = parser.parse_args()

    convert(args.input, args.infmt, args.output, args.outfmt)

