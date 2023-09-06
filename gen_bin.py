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


width, height = 640, 480
background_color = (255, 255, 255)  # 흰 배경

# 헤더 설정
jpeg_info = {
    "dpi": (300, 300),  # 해상도 설정 (dots per inch)
    "quality": 95,      # 이미지 품질 (0~100)
    "progressive": True  # 프로그레시브 JPEG로 설정
}

# 이미지 생성 및 저장
image = Image.new("RGB", (width, height), background_color)
image.save("sample.jpg", "JPEG", **jpeg_info)

exit()

# def hex_to_binary(input_file, output_file):
#     try:
#         with open(input_file, 'r') as hex_file, open(output_file, 'wb') as binary_file:
#             hex_data = hex_file.read().strip()
#             binary_data = bytes.fromhex(hex_data)
#             binary_file.write(binary_data)
#         print(f'Successfully converted {input_file} to {output_file}')
#     except Exception as e:
#         print(f'An error occurred: {str(e)}')


# hex_to_binary('./jpeg/num_0_to_16.txt', 'bin.dat')

# print('done')
# exit()

#-------------------------------------------------------------------------------
# with open('./jpeg/ja.jpg', 'rb') as f, open('bin.dat', 'wb') as fp_w:
#     while True:
#         data = f.read(1)
#         # data = struct.pack('B', data)
#         if data==b'\t':
#             data = struct.pack('B', 9)
#             # fp_w.write(b'0')
#         if data==b'\n':
#             data = struct.pack('b', 9)
#             # fp_w.write(b'0')
#         fp_w.write(data)
#         if data==b'':
#             break
#         print(data)
# exit()

#-------------------------------------------------------------------------------
ptr_out = open('bin.dat', 'wb')
for num in range(16):

    # print('{0} {1}'.format(num, struct.pack('B', num)))

    # if num==10:
    #     data = struct.pack('s', 'a')
    #     ptr_out.write(data)
    #     # ptr_out.write(data)
    # else:
    #     data = struct.pack('B', num)
    #     ptr_out.write(data)

    data = struct.pack('B', num)
    ptr_out.write(data)

exit()



#-------------------------------------------------------------------------------
ptr_out = open('bin.dat', 'wb')
for num in range(16):
    # print(num)
    print('{0} {1}'.format(num, struct.pack('B', num)))

    # if num==10:
    #     imsi = '10'.encode('utf-8') #euc-kr
    #     binary_data = bytes(imsi)
    #     ptr_out.write(binary_data)
    #     # ptr_out.write(data)
    # else:
        # data = struct.pack('B', num)
        # ptr_out.write(data)

    data = struct.pack('B', num)
    ptr_out.write(data)

exit()

#-------------------------------------------------------------------------------
header = open('./jpeg/header_format.txt', 'r')
# header = open('./jpeg/imsi.txt', 'r')
ptr_out = open('bin.dat', 'wb')
for n, num in enumerate(header.readlines()):
    if n%2==0:
        d0 = int(num.strip(), 16)
    elif n%2==1:
        d1 = int(num.strip(), 16)
        data = struct.pack('BB', d0, d1)
        ptr_out.write(data)

ptr_out.close()
exit()


#-------------------------------------------------------------------------------
header = open('./jpeg/header_format.txt', 'r')
# header = open('./jpeg/imsi.txt', 'r')
ptr_out = open('bin.dat', 'wb')
for n, num in enumerate(header.readlines()):
    num = int(num.strip(), 16)
    if num==9:
        data = struct.pack('B', 9)
    elif num==10:
        data = struct.pack('B', 9)
    else:
        data = struct.pack('B', num)
    # print('{0} {1}'.format(num, data))
    ptr_out.write(data)

ptr_out.close()
exit()












# if os.path.isfile(args.i)==False:
#     print ("[LOG] *E, Can not find input file = ", args.i)
#     exit()




# ptr_in = open(args.i, 'r')


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

print(ord('a'))
print('---')
print(chr(15))
print('==========')
exit()


data = struct.pack('BBB', 9, 10, 11)
print(data)
# exit()
# imsi = '91'
# binary_data = bytes.fromhex(imsi)
# print(binary_data)
# exit()
# header = open('./jpeg/header_format.txt', 'r')
ptr_out = open(args.o, 'wb')
# data = struct.pack('BBBB', 9, 10, 11, 12)
# print(data)
data = b"\x08\x09\x0A\x0b\x0c"
ptr_out.write(data)

# l = [8, 9, 10, 11]

# ptr_out.write(bytes(l))

#ptr_out.write(b'\x08\x09')
# for n, num in enumerate(header.readlines()):
#     num = int(num.strip(), 16)
#     data = struct.pack('B', num)
#     print('{0} {1}'.format(num, data))
#     ptr_out.write(data)

ptr_out.close()
exit()


# header = open('./jpeg/header_format.txt', 'w')

# for i in range(0, 16):
#     i = hex(i)[2:]
#     for j in range(0, 16):
#         j = hex(j)[2:]
#         header.write('{0}{1}\n'.format(i, j))
# #     num = int(num.strip(), 16)
# #     data = struct.pack('B', num)
# #     print('{0} {1}'.format(num, data))
# #     ptr_out.write(data)

# # ptr_out.close()
# exit()





header = open('./jpeg/header_format.txt', 'r')
ptr_out = open(args.o, 'wb')
for n, num in enumerate(header.readlines()):
    num = int(num.strip(), 16)
    data = struct.pack('B', num)
    print('{0} {1}'.format(num, data))
    ptr_out.write(data)

ptr_out.close()
exit()




with open('./jpeg/header_format.txt') as f, open('bin.dat', "wb") as fout:
    for line in f.readlines():
        fout.write(
            # binascii.unhexlify(''.join(line.split()))
            bytes((line))
        )

exit()

message = "06 07 08 09 0a 0b 0c 0d 0e 0f"
binary_txt = " ".join(format(ord(c), "b") for c in message)
#for i in binary_txt.split(" "):
for i in message.split(" "):
    i = i.strip()
    print(i)
    i = struct.pack('cc', i[:1], i[1:])
#     i = chr(int(i, 2))
#     print(i)
# #     print(i)
    ptr_out.write(i)
# ptr_out.close()
print(binary_txt)
exit()

# normal = "".join(chr(int(c, 2)) for c in binary_txt.split(" "))

# print(normal)

# message = "Hello Word! This is my message!"
# binary_txt = " ".join(format(ord(c), "b") for c in message)

# normal = "".join(chr(int(c, 2)) for c in binary_txt.split(" "))

# print(normal)
# exit()

# binfile = open('bin.dat', 'wb')

# for num in range(50):
#     data = struct.pack('B', num)
#     binfile.write(data)

# exit()
print('hi')
with open('./jpeg/header_format.txt', 'r') as header, open('bin.dat', 'wb') as binfile:

    for txt_hex in header.readlines():
        txt_hex = txt_hex.strip()
        txt_int = str(int(txt_hex, 16))
        print('----')
        print(txt_int)
        #txt_bin = format(ord(txt_hex[1:]), "b")
        txt_bin = format(ord(txt_int), "b")
        print(txt_bin)

    # hex_data = header.read().strip()
    # bin_data = bytes.fromhex(hex_data)
    # binfile.write(bin_data)


# with open('./jpeg/header_format.txt', 'r') as header, open('bin.dat', 'wb') as binfile:
#     hex_data = header.read().strip()
#     bin_data = bytes.fromhex(hex_data)
#     binfile.write(bin_data)



    # print('{0} {1} {2} {3}'.format(n, num, i, data))
    # ptr_out.write(data)

# for n, i in enumerate(header.readlines()):
#     # i = i.strip()
#     # num = int(i, 16)
#     print(i)
#     data = bytes.fromhex(i)
#     ptr_out.write(data)
#     if n>32:
#         break


# for i in range(16):
#     tmp = '{0}'.format(hex(i))[2:]
#     tmp = '0'+tmp

#     print(tmp)
#     data = bytes.fromhex(tmp)
#     ptr_out.write(data)

ptr_out.close()


# print (" - Write file name : ", args.o)
# print (" - Number of bins : ", NUM_OF_BIN)
print ("Done...")
    