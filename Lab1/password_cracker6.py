#To further improve security, password files usually do not contain the hash of the password PWx of user x. 
# Instead, the password file contains two values for each user x: a random value saltx , called salt, and the 
# result of hashing of a combination of the password PW¬x and of the salt. In this question, you are given a file 
# SaltedPWs which contains, for each user x, the pair (saltx , h(PWx+saltx)), where saltx is a random value chosen for user x.
# Write a new program, Break6.py, that uses the file SaltedPWs to find the passwords of as many gang members as 
# possible that use passwords from PwnedPWs100K concatenated with two random digits, as quickly as possible. 
# Break6 should also save a file containing the names and corresponding passwords. Confirm the exposures using Login.pyc.
import time
import os
import hashlib
    
if __name__ == '__main__':
    start = time.time()
    common_passwords=[i.strip() for i in open('/home/cse/Lab1/PwnedPWs100k.txt')]
    gang_names=[i.strip() for i in open('/home/cse/Lab1/gang.txt')]
    salted_passwords = [i.strip() for i in open('/home/cse/Lab1/Q6/SaltedPWs')]

    hashed_passwords = {}
    for i in salted_passwords:
        if i.split(',')[0] in gang_names:
            hashed_passwords[i.split(',')[1]] = i.split(',')[0] + i.split(',')[2]

    new_passwords = {}
    for i in common_passwords:
        for j in range(100):
            new_passwords[i + str(j)] = hashlib.sha256(bytes(i + str(j) + hashed_passwords[i.split(',')[1]], 'utf-8')).hexdigest()

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
                    print(name, i[1], "--- %s seconds ---" % (time.time() - start))