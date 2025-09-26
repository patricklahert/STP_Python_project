"""Exercise 2.1 """

def gen_blocks(dna_string, blocks_row):
    """function to print out dna ssequence in genbank format"""
    block_size = 10
    count = 0
    block_count = 0
    newline = True

    for base in range(len(dna_string)):

        if count == 0: 

            """adds spaces to fix allignment of index"""
            if newline == True:
                if (base + 1) < 10:
                    print(end=" ")
            if newline == True:
                if (base + 1) < 100:
                    print(end=" ")
            if newline == True:
                if (base + 1) < 1000:
                    print(end=" ")

            """prints index"""
            if newline == True:
                print((base + 1), end=" ")
            
            """print blocks"""
            print(dna_string[base:base + block_size], end=" ") #prints the blocks
            count += block_size
            block_count += 1
            newline = False 

            if block_count == blocks_row: #starts a new line when limit reached
                print("")
                block_count = 0
                newline =True
        count -= 1

if __name__ == "__main__":
    gen_blocks("GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCdCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTAGTCAACTTGTTGAAGAGCTATTGAAAATCATTTGTGCTTTTCAGCTTGACACAGGTTTGGAGTATGCAAACAGCTATAATTTTGCAAAAAAGGAAAATAACTCTCCTGAACATCTAAAAGATGAAGTTTCTATCATCCAAAGTATGGGCTACAGAAACCGTGCCAAAAGACTTCTACAGAGTGAACCCGAAAATCCTTCCTTGCAGGAAACCAGTCTCAGTGTCCAACTCTCTAACCTTGGAACTGTGAGAACTCTGAGGACAAAGCAGCGGATACAACCTCAAAAGACGTCTGTCTACATTGAATTGGGATCTGATTCTTCTGAAGATACCGTTAATAAGGCAACTTATTGCAGTGTGGGAGATCAAG",6)