"""Exercise 1.4"""


def blocks(dna_seq, block_limit):
    """Function to print out a dna string in blocks of specified size"""

    current_block = "" #variable to store bases

    for i in dna_seq:
        current_block += i
        if len(current_block) == block_limit: # when current block reaches the right size it will be printed and reset
            print(current_block, end = " ")
            current_block = ""


if __name__ == "__main__":
    blocks("GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTAC" \
    "AAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTT" \
    "ATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTGAT", 3)