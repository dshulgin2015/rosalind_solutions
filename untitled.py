
#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.
Problem Title: Inferring mRNA from Protein
Rosalind ID: MRNA
Rosalind #: 017
URL: http://rosalind.info/problems/mrna/
'''

import os

def ProteinDictRNA():
    '''Returns a dictionary that translates RNA to Protein.'''
    # Get the raw codon table.
    with open(os.path.join(os.path.dirname(__file__), 'codon_table_rna.txt')) as input_data:
        rna_to_protein = [line.strip().split() for line in input_data.readlines()]

    # Convert to dictionary.
    rna_dict = {}
    for translation in rna_to_protein:
        rna_dict[translation[0]] = translation[1]

    return rna_dict


with open('GRPH.txt') as input_data:
    protein = input_data.read().strip()

# Dictionary translating RNA to Protein
rna_dict = ProteinDictRNA()
rna_num = rna_dict.values().count('Stop')

for p in protein:
    rna_num = rna_num * rna_dict.values().count(p) % 1000000

print rna_num