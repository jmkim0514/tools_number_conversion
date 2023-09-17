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
# example
# crop_bin.py -i ./jpeg/test_192x192.jpg -o ./jpeg/test_192x192_data.bin -s 0x26f
#===============================================================================



import argparse
import struct

parser = argparse.ArgumentParser(description="Crop Binary File")
parser.add_argument('-i', required=True, metavar="input_file", help="Input File (Binary File Format)")
parser.add_argument('-o', required=True, metavar="output_file", help="Output File (Binary File Format)")
parser.add_argument('-s', required=False, metavar="start_of_num", default=0, help="crop number (support hex 0x10)")
parser.add_argument('-e', required=False, metavar="end_of_num", default='eof', help="crop number (support hex 0x10)")

args = parser.parse_args()
input_file = args.i
output_file = args.o
n_start = args.s
n_end = args.e

# input_file = './jpeg/ja.jpg'
# num_start = 608 + 15 # 0x260 + 14

if type(n_start)==str:
    if n_start.isdigit():
        n_start = int(n_start)
    elif n_start.startswith("0x"):
        n_start = int(n_start[2:], 16)
    else:
        print('[LOG] *E, Unknown -s arg = '+n_start)

if type(n_end)==str:
    if n_end=='eof':
        pass
    elif n_end.isdigit():
        n_end = int(n_end)
    elif n_end.startswith("0x"):
        n_end = int(n_end[2:], 16)
    else:
        print('[LOG] *E, Unknown -s arg = '+n_end)

cnt = 0
with open(input_file, 'rb') as p_rd, open(output_file, 'wb') as p_wr:
    while True:
        data = p_rd.read(1)
        if data==b'':
            break

        if cnt>=n_start and (n_end=="eof" or cnt<n_end):
            # print('{0} {1} {2}'.format(data, ord(data), hex(ord(data))[2:]))
            hex_data = format(hex(ord(data))[2:])
            data = int(hex_data, 16)
            data = struct.pack('B', data)
            p_wr.write(data)

        cnt = cnt + 1

print ("===============================================")
print (" crop binary file :")
print ("===============================================")
print (' - Input File : ', input_file)
print (' - Output File : ', output_file)
print (' - Start of Line : ', n_start)
print (' - End of Line : ', n_end)
print (' Done...')
exit()

