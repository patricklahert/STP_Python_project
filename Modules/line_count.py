"""exercise 3.1"""

def count_lines(filename,amino_code):
    """ function to open file and count number of lines"""

    line_count = 0
    aa_count = 0
    amino_code = amino_code.upper()

    if len(amino_code) == 3:
        with open(filename) as file:
        

            for line in file:
                line_count += 1
                if line.count(amino_code) != 0:
                    aa_count += 1
                    print(line)


        if aa_count == 0: 
            print("Amino Acid code not found")  
        print(f"Number of lines in file: {line_count}")
    else:
        print("error please provide a 3 letter code")

count_lines(input("Enter filename: "),input("Enter an Amino Acid code: "))


