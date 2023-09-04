#!/user/de03/DE/util/anaconda3/bin/python3
#===============================================================================
#  File name   : convert_num_hex2bin.py
#  Version     : v0p0
#  Description : convert hexadecimal to binary
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
import struct

parser = argparse.ArgumentParser(description="Generate JPEG Header : ")
# parser.add_argument('-i', metavar="file_path", required=True, help="Input image file path (text file (hex))")
parser.add_argument('-o', metavar="file_path", required=True, default='output.jpg', help="Output JPEG File Path (default=output.bin)")
# parser.add_argument('-w', metavar="width", required=True, help="Image Width")
# parser.add_argument('-h', metavar="height", required=True, help="Image Height")
# #parser.add_argument('-u', action="store_true", help="Prints hex values in uppercase. (default=lowercase)")
args = parser.parse_args()

# if os.path.isfile(args.i)==False:
#     print ("[LOG] *E, Can not find input file = ", args.i)
#     exit()


header = open('./jpeg/header_format.txt', 'r')

# ptr_in = open(args.i, 'r')
ptr_out = open(args.o, 'wb')

# __DEBUG__ = False
# NUM_OF_BIN = int(args.on)
# OBIT = int(NUM_OF_BIN/4)

#------------------------------------------------------------------------------
# Function
#------------------------------------------------------------------------------
# def write_file(istr):
#     """Prints the 'istr' as much as NUM_OF_BIN size and Returns the remaining 'istr'
    
#     Args:
#       istr : input string (hexadecimal)
    
#     Return:
#        Remaining 'istr'
#     """
#     if __DEBUG__:
#       print ("========")
#       print (istr)

#     while (len(istr)*4)>=NUM_OF_BIN:
#         out_str = bin(int(istr[-OBIT:], 16))[2:] #.zfill(NUM_OF_BIN)
#         if __DEBUG__: print("{0:0>{1}}".format(out_str, NUM_OF_BIN))
#         ptr_out.write("{0:0>{1}}\n".format(out_str, NUM_OF_BIN))
#         istr = istr[:-OBIT]
#     return istr

#------------------------------------------------------------------------------
# main
#------------------------------------------------------------------------------

# line = ""z
# for line_new in ptr_in.readlines():
#     if line_new.endswith('\n'):
#         line_new = line_new[:-1]
    
#     line = line_new + line
    
#     line = write_file(line)
    
# ptr_in.close()
# ptr_out.close()

print ("===============================================")
print (" Generate JPEG Header")
print ("===============================================")

for n, i in enumerate(header.readlines()):
    i = i.strip()
    # print(int(i, 16))
    num = int(i, 16)
    
    data = struct.pack('B', num)
    print('{0} {1} {2} {3}'.format(n, num, i, data))
    ptr_out.write(data)




ptr_out.close()


# print (" - Write file name : ", args.o)
# print (" - Number of bins : ", NUM_OF_BIN)
print ("Done...")
    