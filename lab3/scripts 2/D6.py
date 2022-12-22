import os
import sys
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Cipher import PKCS1_OAEP

if __name__ == "__main__":
    encrypted = sys.argv[1]

    decryption_key = sys.stdin.read()

    decryptor = PKCS1_v1_5.new(decryption_key)
    decrypted = decryptor.decrypt(encrypted, None)

    file_out = open(sys.argv[1].replace(".encrypted", ""), "wb")
    file_out.write(decrypted)
    file_out.close()