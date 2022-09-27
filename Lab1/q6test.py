import os
import time
import hashlib

if __name__ in '__main__':
    start_time = time.time()

    gang_names = [i.strip() for i in open('/home/cse/Lab1/gang.txt')]
    salted = [i.strip() for i in open('/home/cse/Lab1/Q6/SaltedPWs')]
    common_passwords = [i.strip() for i in open('/home/cse/Lab1/PwnedPWs100k.txt')]

    salted_passwords = dict((i.split(',')[1], i.split(',')[2]) for i in salted if i.split(',')[0] in gang_names)
    
    new_pass = {}
    for password in common_passwords:
        for rand in range(9,100):
            for ps in salted_passwords:         
                new_pass[password+str(rand)]=hashlib.sha256(bytes(((password + str(rand))+salted_passwords[ps]), 'utf-8')).hexdigest()[2:-1]

    matches = [new_pass[name] for name in new_pass for l in salted_passwords if new_pass[name] == l]
    passwords = [pw for pw in new_pass for match in matches if new_pass[pw] == match]

    for name in gang_names:
        for pw in passwords:
            print(os.system('python3 ./Login.pyc'+ ' ' + name + ' ' + pw) )
            print(name,pw, "--- %s seconds ---" % (time.time() - start_time))
      
            
