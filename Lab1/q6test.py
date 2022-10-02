import os
import time
import hashlib

if __name__ in '__main__':

    print(time.time())

    f1 = open('/home/cse/Lab1/gang.txt', 'r')
    f2 = open('/home/cse/Lab1/Q6/SaltedPWs', 'r')
    f3 = open('/home/cse/Lab1/PwnedPWs100k.txt', 'r')

    names = []
    for i in f1:
        names.append(i.strip())

    salted = []
    for i in f2:
        salted.append(i.strip())

    one_hundred_k = []
    for i in f3:
        one_hundred_k.append(i.strip())

    f1.close()
    f2.close()
    f3.close()

    salt = {}
    for i in salted:
        if i.split(',')[0] in names: salt[i.split(',')[1]] = i.split(',')[2]

    password1 = {}
    for password in one_hundred_k:
        for i in range(1,99):
            for ps in salt:    
                s = salt[ps]
                ran = password+str(i)   
                word = hashlib.sha256(bytes((ran+s), 'utf-8')).hexdigest()
                password1[ran]=word[2:-1]

    m = []
    for name,password in password1.items():
        for salted_p in salt:
            if password == salted_p: 
                print(name,password)
                m.append(salted_p)

    # p = []
    # for a,b in password1.items():
    #     for match in m:
    #         if b == match: p.append(a)

    # for name in names:
    #     for pw in p:
    #         os.system('python3 ./Login.pyc'+ ' ' + name + ' ' + pw)
    #         print(name,pw)

    print(time.time())
      
            
