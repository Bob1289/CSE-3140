import subprocess
import time
import random
import hashlib


start_time = time.time()
common_passwords=[i.strip() for i in open('/home/cse/Lab1/PwnedPWs100k.txt')]
gang_names=[i.strip() for i in open('/home/cse/Lab1/gang.txt')]
salted_passwords = [i.strip() for i in open('/home/cse/Lab1/Q6/SaltedPWs')]

spws = {}
for line in salted_passwords:
    splitline = line.split(',')
    if splitline[0] in gang_names:
        spws[splitline[1]]= splitline[2]

#Hashed and Salted passwords
npw = {}
for pw in common_passwords:
    for i in range(99):
        for a, b in spws.items():        
            p = pw + str(i)
            saltpass = p+b    
            p = hashlib.sha256(bytes(saltpass, 'utf-8'))
            p = p.hexdigest()
            hashed = p[2:-1]
            npw[pw+str(i)]=hashed

#Hashed matches between Salted Passwords and generated passwords
hashedmatches = []
for name, hp in npw.items():
    for l, d in spws.items():
        if hp == l:
            hashedmatches.append(l)

#retrieving original passwords
originalpws = []

for k, v in npw.items():
    for hashedmatch in hashedmatches:
        if v == hashedmatch:
            originalpws.append(k)

for i in gang_names:
    for j in originalpws:
        if subprocess.call(['python3', './Login.pyc', i, j]) == 0:
            print(i, j, "--- %s seconds ---" % (time.time() - start_time))