# Acids and proteins

## Description

mRNA is a molecule that contain the instructions to direct cells on how to make a protein. Codons are groups of three bases (CGAT in this case) in mRNA, each corresponding
to a particular amino acid. These amino acids are chained together to form a protein. There are some additional codons either side of the amino acid chains
in the sequence. The subsequence defining the amino acid chain begins with the 'ATG' codon, and stops the first time is encounters a 'TAA', 'TAG', or 'TGA' codon.
Additionally, instructions can sit within one of three 'reading frames', that begin from the first, second, or third base in the sequence.
Discover the valid subsequence with a length greater than 400. The name of the protein it creates is the flag (three words). Create your flag using the following pattern: ASDCTF{word1_word2_word3}

In the attached files,
- codon_table.txt contains the mapping of codons to amino acids
- mRNA_sequence.txt contains the sequence.
- You will find https://blast.ncbi.nlm.nih.gov/blast/Blast.cgi?PROGRAM=blastp useful once you have discovered the amino acid chain.

## Files

* [codon_table.txt](files/codon_table.txt)

* [mRNA_sequence.txt](files/mRNA_sequence.txt)

