# Look in the Q5files subdirectory and you will find the 
# R5.py and encrypted content files. Your goal is, again, 
# to write a decryption program, D5.py. As in question 4, 
# you are lucky to have the code of R5.py, and even more 
# lucky in that this ransomware turns out, again, to use 
# a symmetric (shared key) cryptosystem. 

# However, your task is a bit more challenging, 
# since the new ransomware, R5.py, is obfuscated, 
# namely, written intentionally in a way designed to make 
# it harder to understand the program – and to find the key, 
# as required to decrypt the file. Obfuscation is an 
# interesting and challenging subject, and used quite a lot 
# in cybersecurity; in this question, the obfuscation is quite weak, 
# so it should not be too hard to break, and write a new decryption program, D5.py.
# R5.py can be found in this directory

# Use R5.py to write a decryption program, D5.py, 
# that can decrypt the encrypted files in the Q5files subdirectory.
# You are not given the key, only the program, R5.py, which is used to encrypt the files.
# import math
# from Crypto.Cipher import AES
# import binascii
# from Crypto.Util.Padding import pad
# import time 
# from Crypto.Random import get_random_bytes 
# import socket
# import sys
# from Crypto.Hash import MD5

# def MyChecksum(hexlist):
#     summ=0
#     carry=0
#     for i in range(0,len(hexlist),2):
#         summ+=(hexlist[i]<< 8)  + hexlist[i+1]
#         carry=summ>>16
#         summ=(summ & 0xffff)  + carry
#     while( summ != (summ & 0xffff)):
#         carry=summ>>16
#         summ=summ & 0xffffffff  + carry
#     summ^=0xffff 
#     return summ
# myHost = 'localhost'
# myPort = 50007
# BLOCKSIZE = 64
# h = MD5.new()
# count = 0

# with open( 'R5.py' , 'rb') as afile:
#     buf = afile.read(BLOCKSIZE)
#     while len(buf) > 0:
#         count = count + 1
#         h.update(buf)
#         buf = afile.read(BLOCKSIZE)
# hf = h.digest()
# bird = hf
# hawk = str(bird)
# of2 = '.key.txt'
# file_out = open(of2, "w") 
# file_out.write("") # Write the varying length ciphertext to the file (this is the encrypted data)
# file_out.close()
# iF = 'p2.txt' # Input file
# oUt = 'e2e2.txt' #outputted cipher text (can rename)
# fin = open(iF, 'rb')
# chicago = fin.read()
# n = 23
# f2 = 1
# for i in range(1,n+1):
#     f2 = f2 * i
# fin.close() 
# detroit = AES.new(bird, AES.MODE_CBC)  #  cipher
# ogD = detroit.encrypt(pad((chicago), AES.block_size))
# fon = open(oUt, "wb")
# fon.write(detroit.iv)
# fon.write(ogD)
# fon.close()
# print('OK')

# try:
#     server_sock = socket.socket(
#             socket.AF_INET, socket.SOCK_STREAM)
#     server_sock.connect((myHost, myPort))
# except OSError as e:
#     if server_sock:
#         server_sock.close()
# #    sys.exit(1)

import os
import sys
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes 
        
file_in = open('e2e2.txt', 'rb')
iv = file_in.read()

original_data = file_in.read()
file_in.close()

file_in = open('.key.txt', 'rb')
variable = file_in.read()
file_in.close()

cipher = AES.new(b'\xb9E\xbd\xce\xaa\xb1F\x13L\xb6q\x9b\x86U~\xe4', AES.MODE_CBC, iv=iv)
ciphered_data = cipher.decrypt(original_data)
print(ciphered_data)




    

