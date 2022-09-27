import time
import os
import hashlib

if __name__ in '__main__': 
    start = time.time()
    print(start)
    f1 = open('/home/cse/Lab1/PwnedPWs100k.txt')
    f2 = open('/home/cse/Lab1/gang.txt')
    f3 = open('/home/cse/Lab1/Q5/HashedPWs')
    hundred=[]
    for i in f1:
        hundred.append(i.strip())
    
    gang=[]
    for i in f2:
        gang.append(i.strip())

    hashed=[]
    for i in f3:
        hashed.append(i.strip())

    hashed_passwords = {}
    for i in hashed:
        if i.split(',')[0] in gang:
            hashed_passwords[i.split(',')[1]] = i.split(',')[0]

    new_passwords = {}
    for i in hundred:
        for j in range(100):
            new_passwords[i + str(j)] = hashlib.sha256(bytes(i + str(j), 'utf-8')).hexdigest()

    matched = []
    for name in hashed_passwords:
        for p in new_passwords:
            if hashed_passwords[name] == new_passwords[p]:
                matched.append((name, p))


    password = []
    for name in new_passwords:
        for match in matched:
            if name == match[1]:
                password.append((match[0], name))

    for name in hashed_passwords:
        for passw in password:
            if name == passw[0]:
                if os.system('python3 ./Login.pyc'+ ' ' + name + ' ' + i[1]) == 0:
                    print(name, passw[1])
                    break

    print(time.time() - start)
           


        




