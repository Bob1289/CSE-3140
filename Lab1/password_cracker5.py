import time
import os
import threading
import hashlib

if __name__ in '__main__':
    start_time = time.time()
    common_passwords=[i.strip() for i in open('/home/cse/Lab1/PwnedPWs100k.txt')]
    gang_names=[i.strip() for i in open('/home/cse/Lab1/gang.txt')]
    hashed_pws = [i.strip() for i in open('/home/cse/Lab1/Q5/HashedPWs')]
    hashed_pws = dict(i.split(',') for i in hashed_pws)
    for name in gang_names:
        gang_hashed = []
        if name in hashed_pws:
            gang_hashed.append(hashed_pws[name])


    new_common_hashed_passwords = []
    for passwords in common_passwords[:10000]:
        for i in range(10,99):
            ps = passwords + str(i)
            new_common_hashed_passwords.append(hashlib.sha256(ps.encode('utf-8')).hexdigest())

    for gangmember in gang_hashed:
        for i in new_common_hashed_passwords:
            if i == gangmember:
                print(gangmember, i, "--- %s minutes ---" % ((time.time() - start_time) / 60))
                break


        




