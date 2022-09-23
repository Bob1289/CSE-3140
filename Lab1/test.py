
import os
import hashlib

if __name__ in '__main__':
    string = '123456'
    print(hashlib.sha256(string.encode('utf-8')).hexdigest())

