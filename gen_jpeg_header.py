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

JPEG_HEADER = """
ff d8 ff e0 00 10 4a 46 49 46 00 01 01 00 00 01
00 01 00 00 ff db 00 43 00 01 01 01 01 01 01 01
01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01
01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01
01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01
01 01 01 01 01 01 01 01 01 ff db 00 43 01 01 01
01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01
01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01
01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01
01 01 01 01 01 01 01 01 01 01 01 01 01 01 ff c0
00 11 08 {0} {1} 03 01 11 00 02 11 01 03 11
01 ff c4 00 1f 00 00 03 01 01 01 01 01 01 01 01
01 00 00 00 00 00 00 01 02 03 04 05 06 07 08 09
0a 0b ff c4 00 b5 10 00 02 01 03 03 02 04 03 05
05 04 04 00 00 01 7d 01 02 03 00 04 11 05 12 21
31 41 06 13 51 61 07 22 71 14 32 81 91 a1 08 23
42 b1 c1 15 52 d1 f0 24 33 62 72 82 09 0a 16 17
18 19 1a 25 26 27 28 29 2a 34 35 36 37 38 39 3a
43 44 45 46 47 48 49 4a 53 54 55 56 57 58 59 5a
63 64 65 66 67 68 69 6a 73 74 75 76 77 78 79 7a
83 84 85 86 87 88 89 8a 92 93 94 95 96 97 98 99
9a a2 a3 a4 a5 a6 a7 a8 a9 aa b2 b3 b4 b5 b6 b7
b8 b9 ba c2 c3 c4 c5 c6 c7 c8 c9 ca d2 d3 d4 d5
d6 d7 d8 d9 da e1 e2 e3 e4 e5 e6 e7 e8 e9 ea f1
f2 f3 f4 f5 f6 f7 f8 f9 fa ff c4 00 1f 01 00 03
01 01 01 01 01 01 01 01 01 00 00 00 00 00 00 01
02 03 04 05 06 07 08 09 0a 0b ff c4 00 b5 11 00
02 01 03 03 02 04 03 05 05 04 04 00 00 01 7d 01
02 03 00 04 11 05 12 21 31 41 06 13 51 61 07 22
71 14 32 81 91 a1 08 23 42 b1 c1 15 52 d1 f0 24
33 62 72 82 09 0a 16 17 18 19 1a 25 26 27 28 29
2a 34 35 36 37 38 39 3a 43 44 45 46 47 48 49 4a
53 54 55 56 57 58 59 5a 63 64 65 66 67 68 69 6a
73 74 75 76 77 78 79 7a 83 84 85 86 87 88 89 8a
92 93 94 95 96 97 98 99 9a a2 a3 a4 a5 a6 a7 a8
a9 aa b2 b3 b4 b5 b6 b7 b8 b9 ba c2 c3 c4 c5 c6
c7 c8 c9 ca d2 d3 d4 d5 d6 d7 d8 d9 da e1 e2 e3
e4 e5 e6 e7 e8 e9 ea f1 f2 f3 f4 f5 f6 f7 f8 f9
fa ff da 00 0c 03 01 00 02 11 03 11 00 3f 00"""


def is_text_file(file_path, num_bytes=512):
    try:
        with open(file_path, 'rb') as file:
            content = file.read(num_bytes)
        if b'\x00' in content:  # 이진 데이터에 널 바이트가 포함되어 있을 수 있으므로 확인
            return False
        # UTF-8으로 디코딩하여 에러가 발생하지 않으면 텍스트로 간주
        content.decode('utf-8')
        return True
    except (UnicodeDecodeError, FileNotFoundError):
        return False

def get_int(digit_i):
    if type(digit_i)==int:
        return digit_i
    elif type(digit_i)==str:
        if digit_i.isdigit()         : return int(digit_i)
        elif digit_i.startswith("0x"): return int(digit_i[2:], 16)
        else:
            print('[LOG] *E, Not Supported Number Format = '+digit_i)
            print('[LOG] Supported Format Example : 10, 0xa')
            exit()
    else:
        print('[LOG] *E, Not Supported Number Format = '+digit_i)
        print('[LOG] Supported Format : (int), (str)')
        exit()

def get_hex2(data_i):
    data = hex(data_i)[2:]
    result = '{0:0>4}'.format(data)
    result = result[:2]+' '+result[2:]
    return result

def get_header(width_i, height_i):
    width = get_hex2(get_int(width_i))
    height = get_hex2(get_int(height_i))
    return JPEG_HEADER.format(width, height)

#------------------------------------------------------------------------------
# Main - @mark
#------------------------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate JPEG Header", add_help=False)
    parser.add_argument('-i', required=True, metavar="input_file", help="Input Data File Path, Text Format (str)")
    parser.add_argument('-o', required=True, metavar="output_file", help="Output JPEG File, Binary Format (str)")
    parser.add_argument('-w', required=True, metavar="image_width", help="Image Width (int)")
    parser.add_argument('-h', required=True, metavar="image_height", help="Image Height (int)")
    parser.add_argument('-help', '-help', action='help', default=argparse.SUPPRESS, help='Show this help message and exit')

    # input_file = './jpeg/ja_data.txt'
    # input_file = './jpeg/test1_192x192_data.txt'
    # output_file = './imsi.jpg'
    args = parser.parse_args()
    input_file = args.i
    output_file = args.o
    image_width = args.w
    image_height = args.h


    header = get_header(image_width, image_height)
    print(header)
    exit()
    # gen_jpeg(input_file, output_file, header)


    p_rd = open(input_file, 'r')
    p_wr = open(output_file, 'wb')



    for n, line in enumerate(JPEG_HEADER.split('\n')):
        if line=="":
            continue
        line = line.split(' ')
        # line.reverse()
        # print(line)
        for data in line:
            data = int(data.strip(), 16)
            data = struct.pack('B', data)
            p_wr.write(data)

    for data in p_rd.readlines():
        data = int(data.strip(), 16)
        data = struct.pack('B', data)
        p_wr.write(data)

    p_rd.close()
    p_wr.close()
    print("Done...")
    exit()



# JPEG_HEADER_ORG = """
# ff d8 ff e0 00 10 4a 46 49 46 00 01 01 00 00 01
# 00 01 00 00 ff db 00 43 00 01 01 01 01 01 01 01
# 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01
# 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01
# 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01
# 01 01 01 01 01 01 01 01 01 ff db 00 43 01 01 01
# 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01
# 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01
# 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01
# 01 01 01 01 01 01 01 01 01 01 01 01 01 01 ff c0
# 00 11 08 00 60 00 60 03 01 11 00 02 11 01 03 11
# 01 ff c4 00 1f 00 00 03 01 01 01 01 01 01 01 01
# 01 00 00 00 00 00 00 01 02 03 04 05 06 07 08 09
# 0a 0b ff c4 00 b5 10 00 02 01 03 03 02 04 03 05
# 05 04 04 00 00 01 7d 01 02 03 00 04 11 05 12 21
# 31 41 06 13 51 61 07 22 71 14 32 81 91 a1 08 23
# 42 b1 c1 15 52 d1 f0 24 33 62 72 82 09 0a 16 17
# 18 19 1a 25 26 27 28 29 2a 34 35 36 37 38 39 3a
# 43 44 45 46 47 48 49 4a 53 54 55 56 57 58 59 5a
# 63 64 65 66 67 68 69 6a 73 74 75 76 77 78 79 7a
# 83 84 85 86 87 88 89 8a 92 93 94 95 96 97 98 99
# 9a a2 a3 a4 a5 a6 a7 a8 a9 aa b2 b3 b4 b5 b6 b7
# b8 b9 ba c2 c3 c4 c5 c6 c7 c8 c9 ca d2 d3 d4 d5
# d6 d7 d8 d9 da e1 e2 e3 e4 e5 e6 e7 e8 e9 ea f1
# f2 f3 f4 f5 f6 f7 f8 f9 fa ff c4 00 1f 01 00 03
# 01 01 01 01 01 01 01 01 01 00 00 00 00 00 00 01
# 02 03 04 05 06 07 08 09 0a 0b ff c4 00 b5 11 00
# 02 01 03 03 02 04 03 05 05 04 04 00 00 01 7d 01
# 02 03 00 04 11 05 12 21 31 41 06 13 51 61 07 22
# 71 14 32 81 91 a1 08 23 42 b1 c1 15 52 d1 f0 24
# 33 62 72 82 09 0a 16 17 18 19 1a 25 26 27 28 29
# 2a 34 35 36 37 38 39 3a 43 44 45 46 47 48 49 4a
# 53 54 55 56 57 58 59 5a 63 64 65 66 67 68 69 6a
# 73 74 75 76 77 78 79 7a 83 84 85 86 87 88 89 8a
# 92 93 94 95 96 97 98 99 9a a2 a3 a4 a5 a6 a7 a8
# a9 aa b2 b3 b4 b5 b6 b7 b8 b9 ba c2 c3 c4 c5 c6
# c7 c8 c9 ca d2 d3 d4 d5 d6 d7 d8 d9 da e1 e2 e3
# e4 e5 e6 e7 e8 e9 ea f1 f2 f3 f4 f5 f6 f7 f8 f9
# fa ff da 00 0c 03 01 00 02 11 03 11 00 3f 00"""
