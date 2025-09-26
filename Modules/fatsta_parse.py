"""exercise 4"""

def fasta_parse(filename):
    """function to produce a dictionary of sample names and sample DNA from fasta file"""

    sample_data = {}
    value = ""

    with open(filename) as fasta_file:
        for line in fasta_file:
            if line[0] == ">": #finds sample ID when line starts with ">"
                key = line.replace("\n","") 
                sample_data.update({key:""})
                value = ""
            else:
                value += line.replace("\n","") # adds line to value variable
                sample_data.update({key:value}) #updates dict with dna sequence

    return sample_data #returns dictionary containing sample name and dna sequence
        


