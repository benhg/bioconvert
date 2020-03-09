#!/usr/bin/env python3

"""
Convert a FASTA file to a PHYLIP file
"""
import sys
from Bio import SeqIO


def convert(input_file, output_file):
    with open(input_file, "rU") as input_handle, open(output_file, "w") as output_handle:
        sequences = SeqIO.parse(input_handle, "fasta")
        count = SeqIO.write(sequences, output_handle, "phylip") 
    print(f"Converted {count} sequences.")



if __name__ == '__main__':
    
    if len(sys.argv) != 3:
        print("Usage: fasta2phylip <input file> <output file>")
        exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert(input_file, output_file)

