import os
import json
import argparse

parser = argparse.ArgumentParser(description="Add dummy data for ROMCODE")
parser.add_argument('-i', metavar="file_path", required=True, help="Input Json File")
args = parser.parse_args()

if os.path.isfile(args.i)==False:
    print("[LOG] *E, Can not find json file = ", args.i)
    exit()

with open(args.i, "r") as f:
    opt_json = json.load(f)

input_file_path = opt_json["input_file_path"].strip()
output_file_path = opt_json["output_file_path"].strip()
patterns = opt_json["pattern"]

fp_wr = open(output_file_path, "w")

if len(input_file_path)>0:
    if os.path.isfile(input_file_path)==False:
        print("[LOG] *E, Can not find input file = ", input_file_path)
        exit()

    fp_rd = open(input_file_path, "r")
    for line in fp_rd.readlines():
        line = line.strip()
        if len(line)>0:
            fp_wr.write(line+"\n")

for pattern in patterns:
    value = pattern["value"]
    count = pattern["count"]
    for i in range(int(count)):
        fp_wr.write(value+"\n")

if len(input_file_path)>0:
    fp_rd.close()
fp_wr.close()

#------------------------------------------------------------------------------
# Report
#------------------------------------------------------------------------------
print ("===============================================")
print (" Add dummy data for ROMCODE")
print ("===============================================")
print (" - Config JSON file name : ", args.i)
print (" - Input file name : ", input_file_path)
print (" - Output file name : ", output_file_path)
print ("Done...")
