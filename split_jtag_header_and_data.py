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
import binascii
from binascii import unhexlify
from PIL import Image
import io
import numpy as np


#-------------------------------------------------------------------------------
# ja.jpg --> ja_header.bin, ja_data.bin

input_jpg = './jpeg/ja.jpg'
output_header = './jpeg/ja_header.bin'
output_data   = './jpeg/ja_data.bin'

start_data = 608 + 15 # 0x260 + 14

with open(input_jpg, 'rb') as r_jpg, open(output_header, 'wb') as w_header, open(output_data, 'wb') as w_data:
    i = 0
    while True:
        data = r_jpg.read(1)
        if data==b'':
            break
        if i<start_data:
            w_header.write(data)
        else:
            w_data.write(data)
        
        i = i + 1

print('Done....')
exit()