"""Exercise 2.6 """

def gc_content(dna_input):
    """Fucntion to calculate the GC contemt of a DNA sequence"""

    dna_input = dna_input.upper() # convert sequence to uppercase
    gc_count = 0
    error_count = 0
    gc_result = 0

    for base in dna_input: #loops through input sequence
        if base == "G" or base == "C": #counts g and c in sequence
            gc_count +=1 
        elif base == "A" or base == "T":
            pass
        else: #counts errors if base is not actg
            error_count +=1

    gc_result = ((gc_count)/(len(dna_input))*100 ) #calculates gc content as a percentage
    gc_result = "{:.2f}".format(gc_result) #rounds to two decimal places
    
    if error_count != 0: #prints a message if any errors found
        print(f"Warining {error_count} unknown bases found in the input sequence")

    print(f"GC content: {gc_result}%") #prints the result

    return gc_result







if __name__ == "__main__":
    
    gc_content("GAACCCGAAAATCCTTCCTTGCAGGAAACCAGTCTCAGTGTCCAACTCTCTAACCTTGGAACT" \
    "GTGAGAACTCTGAGGACAAAGCAGCGGATACAACCTCAAAAGACGTCTGTCTACATTGAATTGGGATCTGATTC" \
    "TTCTGAAGATACCGTTAATAAGGCAACTTATTGCAGTGTGGGAGATCAAGAATTGTTACAAATCACCCCTCAAG" \
    "GAACCAGGGATGAAATCAGTTTGGATTCTGCAAAAAAGGCTGCTTGTGAATTTTCTGAGACGGATGTAA")