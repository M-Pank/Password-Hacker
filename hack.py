def hack(ip, port):
    import socket
    hack_sock = socket.socket()
    address = (ip, int(port))
    hack_sock.connect(address)
    import itertools
    a = open('C:/Users/Carbon/PycharmProjects/Password Hacker/Password Hacker/task/hacking/passwords.txt', "r")
    import itertools
    counter = 0
    for i in a:
        if counter != 0:
            break
        i = i.strip("\n")
        psy = i
        search = map(lambda x: ''.join(x), itertools.product(*([letter.lower(), letter.upper()] for letter in psy)))
        for m in search:
            message = m.encode()
            hack_sock.send(message)
            response = hack_sock.recv(1024)
            response = response.decode()
            if response == "Connection success!":
                print(m)
                counter = 1
                break

    hack_sock.close()

import sys

args = sys.argv
hack(args[1], args[2])
