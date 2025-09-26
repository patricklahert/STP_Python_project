"""Exercise 2.5"""

def nucleotide_count(dna_seq):
    """Function to count the single, di and trinucletide bases in a sequence"""
    dna_seq = dna_seq.upper()
    block = ""
    base_dict = {}
    base_error = True
    standard_bases = "ACTG"
   
    for size in range(3): #loops 3 times for single di and tri nucleotides
        for base in dna_seq:
            print(base)
            """error handling"""
            if base.upper() not in standard_bases:
                base_error = True
               
            
            """creates and updates dictionary"""
            block += base 
            if len(block) == (size + 1):
                if block in base_dict.keys(): #if nucluetide in dict 
                    base_dict.update({block:(int(base_dict.get(block))+1)}) #adds 1 to entries
                else:
                    base_dict.update({block:1}) # if not in dictionary - adds it
                block = ""


        """Prints the results"""       
        if size == 0:
            print("Single Nucleotides")
        elif size == 1: 
            print("Di-Nucleotides")
        elif size == 2:
            print("Tri-Nucleotides")
        for entry in base_dict:
            print(f"{entry} : {base_dict.get(entry)}")
        base_dict = {}
    if base_error == True:
        print("Warning non standard bases or gaps detected!")


if __name__ == "__main__":
    nucleotide_count("aggagtaagcccttgcaactggaaatacacccattg")

