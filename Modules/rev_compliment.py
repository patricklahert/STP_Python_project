""" Excercise 2.3"""

def rev_compliment(dna_input):
    """funcction to return reverse compliment of a dna sequence"""
    
    dna_seq = dna_input.lower()
    dna_seq = dna_seq.replace("a","T")
    dna_seq = dna_seq.replace("c","G")
    dna_seq = dna_seq.replace("g","C")
    dna_seq = dna_seq.replace("t","A")
    return dna_seq[::-1]
    



if __name__ == "__main__":
    print(rev_compliment("GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAG" \
    "GCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGT" \
    "TGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGA" \
    "TCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAAC" \
    "CAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAG" \
    "TACGAGATTTGAT"))
    
