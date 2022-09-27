import time
import os
import random
import hashlib

if __name__ in '__main__':
    start_time = time.time()
    common_passwords=[i.strip() for i in open('/home/cse/Lab1/PwnedPWs100k.txt')]
    gang_names=[i.strip() for i in open('/home/cse/Lab1/gang.txt')]
    hashed_pws = [i.strip() for i in open('/home/cse/Lab1/Q5/HashedPWs')]

    hashed_pws = dict(i.split(',') for i in hashed_pws if i.split(',')[0] in gang_names)

    named_pws = dict((i + str(j), hashlib.sha256(bytes(i + str(j), 'utf-8')).hexdigest()) for i in common_passwords for j in range(100))

    matched = []
    for name, hashed in hashed_pws.items():
        for p, h in named_pws.items():
            if hashed == h:
                matched.append((name, p))

    ogpass = []
    for name, p in named_pws.items():
        for i in matched:
            if name == i[1]:
                ogpass.append((i[0], name))

    for name, p in hashed_pws.items():
        for i in ogpass:
            # print out the name and password if the password is correct for the name
            if name == i[0]:
                if os.system('python3 ./Login.pyc'+ ' ' + name + ' ' + i[1] + " >/dev/null 2>&1") == 0:
                    print(name, i[1], "--- %s seconds ---" % (time.time() - start_time))