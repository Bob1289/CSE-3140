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