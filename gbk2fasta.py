#!/usr/bin/env python
# function: converting GenBank file into FASTA file.

# Copy (C) 2018-2019 Massey University. All rights reserved
# Written by Ji Zhang, MD, PhD

# Revision notes

from Bio import SeqIO
import sys

def gbk2fasta(infile, outfile):
    with open(infile, "r") as input_handle, open(outfile, "w") as output_handle:
        sequences = SeqIO.parse(input_handle, "genbank")
        SeqIO.write(sequences, output_handle, "fasta")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python gbk2fasta.py in.gbk out.fas")
        sys.exit(1)

    infile = sys.argv[1]
    outfile = sys.argv[2]
    
    gbk2fasta(infile, outfile)

