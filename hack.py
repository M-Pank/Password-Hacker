def hack(ip, port, message):
    import socket
    hack_sock = socket.socket()
    address = (ip, int(port))
    hack_sock.connect(address)
    message = message.encode()
    hack_sock.send(message)
    response = hack_sock.recv(1024)
    response = response.decode()
    print(response)
    hack_sock.close()
import sys
args = sys.argv
hack(args[1], args[2], args[3])

