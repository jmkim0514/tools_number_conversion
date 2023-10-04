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


# width /16x3
# height /8

width = 16*3
height = 8

i = 0

n0 = list(range(0, 8))
n1 = list(range(64, 64+8))
# print(n0)
# print(n0[0])
# print(n1)
# print(n1[0])


for i, h in enumerate(n0):
    print(i, h)
    


