import sys

class login:
    def __init__(self, id, pas):
        self.id = id
        self.pas = pas

    def check(self, user, password):
        if self.id == user and self.pas == password:
            print("Success: correct userid and password!")
            sys.exit(0)
        else:
            print("Incorrect Login!")
            sys.exit (1)

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print('Bad input, please enter username and password with a space in between')
        sys.exit(2)

    log = login("Adam", "##passwrd")
    log.check(sys.argv[1], sys.argv[2])

