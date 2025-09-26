"""Exercise 4: Open Reading Frames (ORFs)"""

from fatsta_parse import *  
from read_frames import *
from transcription import *
from translation import *
from rev_compliment import *



def orfs(dna_input):
    """function to find all the open reading frames in a given DNA sequence"""
    
    reverse_strand = rev_compliment(dna_input) #get reverse compliment of input strand
    rnaseq = transcription(dna_input) #transcribe input stran
    rev_renaseq = transcription(reverse_strand) #transcribe reverse compliment strand   

    """Forward Strands"""
    for seq in range(3): #loops once for each reading frame
        print(f"Forward Strand Frame {seq + 1}:")
        print(translation(rnaseq[seq:],False)) #translate input strand - false argument to turn off error messages
        print("")
    
    """Reverse Strands"""
    for rev_seq in range(3):
        print(f"Reverse Strand Frame {rev_seq + 1}:")
        print(translation(rev_renaseq[rev_seq:],False)) #translate reverse compliment strand - false argument to turn off error messages
        print("")   
    
    






if __name__ ==  "__main__":
    dna_dict = fasta_parse("U15422.1.fasta") #parses fasta file to get sequence
    for i in dna_dict.values():
        dna_input = i
    orfs(dna_input)

