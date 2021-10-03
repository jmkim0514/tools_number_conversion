# Number Conversion
숫자로 작성된 text file을 다른 숫자 format으로 변형하여 저장한다.
binary와 hexadecimal 숫자 format을 지원한다.

Script Name
- convert_num_bin2hex.py 
- convert_num_hex2bin.py

## convert_num_bin2hex.py 
- hexadecimal을 binary로 저장한다.
- hex로 출력해야 하므로 binary 숫자 갯수가 4 align 되야 한다. 

- 실행명령
  - i : 2진수로 작성된 파일 위치
  - o : 결과 파일 이름, 작성 안하면 "imsi.hex" 파일이름으로 출력
  - on : 한줄에 출력할 hex 값 개수 (eg=1/2/4/8/16/32...)
  - u : hex 값을 대문자로 출력한다. 기본값은 소문자이다.
```
usage: convert_num_bin2hex.py [-h] -i file_path [-o file_path] [-on number]
                              [-u]

Number Conversion : Binary to Hexadecimal

optional arguments:
  -h, --help    show this help message and exit
  -i file_path  Input binary file path
  -o file_path  Output hex file path (default=imsi.hex)
  -on number    Number of hexs (default=8, eg=1/2/4/8/16...)
  -u            Prints hex values in uppercase. (default=lowercase)
```

- example
```
convert_num_bin2hex.py -i ./input/data.bin
convert_num_bin2hex.py -i data.bin -o data.hex
convert_num_bin2hex.py -i data.bin -o data.hex -u
convert_num_bin2hex.py -i data.bin -o data.hex -on 8 -u
```

## convert_num_hex2bin.py 
- binary를 hexadecimal로 저장한다.

- 실행명령
  - i : 2진수로 작성된 파일 위치
  - o : 결과 파일 이름, 작성 안하면 "imsi.bin" 파일이름으로 출력
  - on : 한줄에 출력할 bin 값 개수 (eg=4/8/16/32/..)
```
usage: convert_num_hex2bin.py [-h] -i file_path [-o file_path] [-on number]

Number Conversion : Hexadecimal to Binary

optional arguments:
  -h, --help    show this help message and exit
  -i file_path  Input hex file path
  -o file_path  Output bin file path (default=imsi.bin)
  -on number    Number of bins per line (default=8, eg=4/8/16/32/..)
```

- example
```
convert_num_hex2bin.py -i ./input/data.hex
convert_num_bin2hex.py -i data.hex -o data.bin
convert_num_bin2hex.py -i data.hex -o data.bin -on 16
```
