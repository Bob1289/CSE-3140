
import os

if __name__ in '__main__':
    f1 = open('/home/cse/Lab1/MostCommonPWs.txt','r')
    f2 = open('/home/cse/Lab1/gang.txt', 'r')
    
    names = []
    for i in f2:
        names.append(i.strip())

    passwords = []
    for i in f1:
        passwords.append(i.strip())

    f1.close()
    f2.close()

    for name in names:
        for password in passwords:
            psswrd = os.system('python3 ./Login.pyc'+ ' ' + name + ' ' + password)
            if psswrd == 0:
                print(name, password)
                break


