"""Exercise 2.4"""
import sys
sys.path.append(r'c:\Users\patri\python\Exercise_1')
from Exercise_1_5 import transcription 
from Exercise_2_2 import translation
from Exercise_2_3 import rev_compliment




def read_frames(input_seq,):
    """Function to print forward and reverse reading frames"""


    print("Forward")
    for f_frame in range(3): #loops once for each reading frame
        print((f_frame + 1), translation(input_seq.upper()[f_frame:],False)) #calls fucntion to translate - gives false argument to turn error messages off

    print("Reverse")
    rev_seq = rev_compliment(input_seq.upper()) #calls fucntion to get reverse compliment
    for r_frame in range(3):
        print((r_frame + 1), translation(rev_seq[r_frame:],False))

    


if __name__ ==  "__main__":
    read_frames("aggagtaagcccttgcaactggaaatacacccattg")