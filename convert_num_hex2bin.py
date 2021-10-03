import os
import argparse

parser = argparse.ArgumentParser(description="Number Conversion : Hexadecimal to Binary")
parser.add_argument('-i', metavar="file_path", required=True, help="Input hex file path")
parser.add_argument('-o', metavar="file_path", required=False, default='imsi.bin', help="Output bin file path (default=imsi.bin)")
parser.add_argument('-on', metavar="number", required=False, default='8', help="Number of bins per line (default=8, eg=4/8/16/32/..)")
#parser.add_argument('-u', action="store_true", help="Prints hex values in uppercase. (default=lowercase)")
args = parser.parse_args()

if os.path.isfile(args.i)==False:
    print ("[LOG] *E, Can not find input file = ", args.i)
    exit()

ptr_in = open(args.i, 'r')
ptr_out = open(args.o, 'w')

__DEBUG__ = False
NUM_OF_BIN = int(args.on)
OBIT = int(NUM_OF_BIN/4)

#------------------------------------------------------------------------------
# Function
#------------------------------------------------------------------------------
def write_file(istr):
    """Prints the 'istr' as much as NUM_OF_BIN size and Returns the remaining 'istr'
    
    Args:
      istr : input string (hexadecimal)
    
    Return:
       Remaining 'istr'
    """
    if __DEBUG__:
      print ("========")
      print (istr)

    while (len(istr)*4)>=NUM_OF_BIN:
        out_str = bin(int(istr[-OBIT:], 16))[2:] #.zfill(NUM_OF_BIN)
        if __DEBUG__: print("{0:0>{1}}".format(out_str, NUM_OF_BIN))
        ptr_out.write("{0:0>{1}}\n".format(out_str, NUM_OF_BIN))
        istr = istr[:-OBIT]
    return istr

#------------------------------------------------------------------------------
# main
#------------------------------------------------------------------------------

line = ""
for line_new in ptr_in.readlines():
    if line_new.endswith('\n'):
        line_new = line_new[:-1]
    
    line = line_new + line
    
    line = write_file(line)
    
ptr_in.close()
ptr_out.close()

print ("===============================================")
print (" Number Conversion : Hexadecimal to Binary")
print ("===============================================")
print (" - Write file name : ", args.o)
print (" - Number of bins : ", NUM_OF_BIN)
print ("Done...")
    