""" Exercise 2.2   """
import sys
sys.path.append(r'c:\Users\patri\python\Exercise_1')
from Exercise_1_5 import transcription 


def translation(dna_seq):
    """Function to translate DNA into protein"""

    "Transcribes to rna"
    rna_seq = transcription(dna_seq)


    codons = {"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V", 
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
    for base in rna_seq:
        block += base #adds base in rna to blocks
        if len(block) == 3: 
            try:
                protein_string += codons.get(block) #adds the amino acid to the protein based on block
                block = ""
                continue
            except: # X is added if no codon is found
                protein_string += "X"
                block = ""
                print("Warning unknown codon detected!")
    if len(block) != 0:
        print(f"Incomplete codon containing bases: {block} detected!")
    return(protein_string)
        

if __name__ == "__main__":
    print(translation("ATGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAG" \
    "GAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAA"))