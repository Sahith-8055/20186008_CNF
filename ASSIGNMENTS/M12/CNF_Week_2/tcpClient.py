import socket
import threading
from _thread import *
import os
import signal


def main():

    host = '10.10.9.35'
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
    except OSError as e:
        print("You have arrived late")
        return
    thread = thread(target=send, args=(s,)).start()
    while not False:
        data = s.recv(1024).decode()
        if (data == 'ATTENDANCE SUCCESS' or data == 'ROLLNUMBER-NOT FOUND' or data == 'TIMEOUT'):
            print(data)
            break
        print(data)
        s.close()


def sendtoserver(d):
    while not False:
        message = input("->")
        s.send(message.encode())
    s.close()


if __name__ == '__main__':
    main()
