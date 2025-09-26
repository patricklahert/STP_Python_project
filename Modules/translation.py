""" Exercise 2.2   """

from transcription import transcription 


def translation(dna_seq,error_messages):
    """Function to translate DNA into protein"""

    rna_seq = transcription(dna_seq) #transcribes to rna

    codons = {"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V", #dictionary of codons and the respective protein
           "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
           "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
           "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
           "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
           "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
           "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
           "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
           "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
           "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
           "UAA": "*", "CAA": "Q", "AAA": "K", "GAA": "E",
           "UAG": "*", "CAG": "Q", "AAG": "K", "GAG": "E",
           "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
           "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
           "UGA": "*", "CGA": "R", "AGA": "R", "GGA": "G",
           "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"}


    """translates to protein"""
    block = ""
    protein_string = ""
    codon_errors = 0
    translating = False
    protein_candidates = []
    for base in rna_seq:
        block += base #adds base in rna to blocks
        if len(block) == 3: 
            if block == "AUG": #if codon is start codnon translation starts
                translating = True
            if block == "UAA" or block == "UAG" or block == "UGA": #if stop codon is found translation stops and candidate protein added to list
                translating = False
                protein_candidates.append(protein_string)
                protein_string = ""
            if translating == True:
                try:
                    protein_string += codons.get(block) #adds the amino acid to the protein based on block
                except: # X is added if no codon is found
                    protein_string += "X"
                    codon_errors += 1
            block = ""
            
    if error_messages == True:
        if len(block) != 0:
            print(f"Incomplete codon containing bases: {block} detected!")
        if codon_errors != 0:
            print(f"Warning {codon_errors} unknown codons detected!")

    longest_protein = ""
    for prot in protein_candidates:
        if len(prot) > len(longest_protein):
            longest_protein = prot
    protein_candidates
    return(longest_protein)

if __name__ == "__main__":
    print(translation("CGCTCGGCATTATGCGGCGAGGGGGGCTGCTGGAGGTCGCCTTGGGATTTACCGTGCTCTTAGCGTCCTACACGAGCCATGGGGCGGATACCAATTTGGAGGCTGGGAACGTGAAGGAAACCAGAGCCAACCGGGCCAAGAGAAGAGGTGGCGGAGGACACAACGCGCTTAAAGGACCCAATGTCTGTGGATCACGTTATAATGCTTACTGTTGCCCTGGATGGAAGACTTTACCTGGTGGAAA",True))