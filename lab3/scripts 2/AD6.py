import os
import sys
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Cipher import PKCS1_OAEP

if __name__ == "__main__":
    file_in = open("d.key", "rb")
    private_key = RSA.import_key(file_in.read())
    file_in.close()
    # Read the identifier input
    identifier = sys.argv[1]
    # Decrypt the identifier
    decryptor = PKCS1_OAEP.new(private_key)
    # Find the file with the identifier
    for file in os.listdir():
        if file.endswith(".ID"):
            file_in = open(file, "r")
            message = file_in.read()
            file_in.close()
            if message == identifier:
                # Decrypt the identifier
                decrypted = decryptor.decrypt(message)
                print(decrypted)
                break