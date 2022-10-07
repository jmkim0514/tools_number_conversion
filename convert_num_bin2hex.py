#!/user/de03/DE/util/anaconda3/bin/python3
#===============================================================================
#  File name   : convert_num_bin2hex.py
#  Version     : v0p0
#  Description : convert binary to hexadecimal
#  Simulator   : Python 3
#  Created by  : Kim jong-min
#  Date        : 2021/07/07     1'st Release
#===============================================================================
#  History
#-------------------------------------------------------------------------------
# 2021-07-07 Jongmin-Kim    1st Release
#===============================================================================
import os
import argparse

parser = argparse.ArgumentParser(description="Number Conversion : Binary to Hexadecimal")
parser.add_argument('-i', metavar="file_path", required=True, help="Input binary file path")
parser.add_argument('-o', metavar="file_path", required=False, default='imsi.hex', help="Output hex file path (default=imsi.hex)")
parser.add_argument('-on', metavar="number", required=False, default='8', help="Number of hexs per line (default=8, eg=1/2/4/8/16...)")
parser.add_argument('-u', action="store_true", help="Prints hex values in uppercase. (default=lowercase)")
args = parser.parse_args()

if os.path.isfile(args.i)==False:
    print ("[LOG] *E, Can not find input file = ", args.i)
    exit()

ptr_in = open(args.i, 'r')
ptr_out = open(args.o, 'w')

__DEBUG__ = False
NUM_OF_HEX = int(args.on)
OBIT = 4*NUM_OF_HEX

#------------------------------------------------------------------------------
# Function
#------------------------------------------------------------------------------
def write_file(istr):
    """Prints the 'istr' as much as OBIT size and Returns the remaining 'istr'
    
    Args:
      istr : input string (binary)
    
    Return:
       Remaining 'istr'
    """
    if __DEBUG__:
      print ("========")
      print (istr)

    while len(istr)>=OBIT:
        out_str = hex(int(istr[-OBIT:], 2))[2:]
        if args.u:
            out_str = out_str.upper()

        if __DEBUG__: print("{0:0>{1}}".format(out_str, NUM_OF_HEX))
        ptr_out.write("{0:0>{1}}\n".format(out_str, NUM_OF_HEX))
        istr = istr[:-OBIT]
    return istr

#------------------------------------------------------------------------------
# main
#------------------------------------------------------------------------------

line = ""
for line_new in ptr_in.readlines():
    
    #line_new = ''.join(reversed(line_new))
    #line_new = 
    if line_new.endswith('\n'):
        line_new = line_new[:-1]
    
    line = line_new + line
    
    line = write_file(line)
    
ptr_in.close()
ptr_out.close()



print ("===============================================")
print (" Number Conversion : Binary to Hexadecimal")
print ("===============================================")
print (" - Write file name : ", args.o)
print (" - Number of hexs : ",NUM_OF_HEX)
if args.u:
    print (" - Prints in uppercase")
else:
    print (" - Prints in lowercase")
print ("Done...")
    