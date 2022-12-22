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