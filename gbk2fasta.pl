#!/usr/bin/perl
#function: convert GenBank sequence file to FASTA format sequence file.

#Copy (C) 2018-2019 Massey University. All rights reserved
#Written by Ji Zhang, MD, PhD

#Revision notes

use Bio::SeqIO;

my $usage = "perl gbk2fasta.pl in.gbk out.fasta"; 
my $infile = shift or die $usage; 
my $outfile = shift or die $usage;

my $seqin = Bio::SeqIO->new( -file   => "$infile",
                             -format => 'Genbank',
                           );

my $seqout = Bio::SeqIO->new( -file   => ">$outfile",
                              -format => 'Fasta',
                            );

while (my $inseq = $seqin->next_seq) {
   $seqout->write_seq($inseq);
}
