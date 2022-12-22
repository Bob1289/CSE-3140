import math
from Crypto.Cipher import AES
import binascii
from Crypto.Util.Padding import pad
import time 
from Crypto.Random import get_random_bytes 
import socket
import sys
from Crypto.Hash import MD5

def MyChecksum(hexlist):
    summ=0
    carry=0
    for i in range(0,len(hexlist),2):
        summ+=(hexlist[i]<< 8)  + hexlist[i+1]
        carry=summ>>16
        summ=(summ & 0xffff)  + carry
    while( summ != (summ & 0xffff)):
        carry=summ>>16
        summ=summ & 0xffffffff  + carry
    summ^=0xffff 
    return summ
myHost = 'localhost'
myPort = 50007
BLOCKSIZE = 64
h = MD5.new()
count = 0

with open( 'R5.py' , 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        count = count + 1
        h.update(buf)
        buf = afile.read(BLOCKSIZE)
hf = h.digest()
bird = hf
hawk = str(bird)
of2 = '.key.txt'
file_out = open(of2, "w") 
file_out.write("") # Write the varying length ciphertext to the file (this is the encrypted data)
file_out.close()
iF = 'p2.txt' # Input file
oUt = 'e2e2.txt' #outputted cipher text (can rename)
fin = open(iF, 'rb')
chicago = fin.read()
# n = 23
# f2 = 1
# for i in range(1,n+1):
#     f2 = f2 * i
fin.close() 
detroit = AES.new(bird, AES.MODE_CBC)  #  cipher
ogD = detroit.encrypt(pad((chicago), AES.block_size))
fon = open(oUt, "wb")
fon.write(detroit.iv)
fon.write(ogD)
fon.close()
print('OK')

try:
    server_sock = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
    server_sock.connect((myHost, myPort))
except OSError as e:
    if server_sock:
        server_sock.close()
#    sys.exit(1)