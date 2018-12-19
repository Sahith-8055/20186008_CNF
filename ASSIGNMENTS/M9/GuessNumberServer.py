import socket
import random
import threading
from _thread import *


def Main():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host1 = socket.gethostname()
    host = socket.gethostbyname(host1)
    port = 5010
    s.bind((host, port))
    s.listen(10)
    while True:
        c, addr = s.accept()
        print("Connected Server" + str(addr))
        x = int(random.randint(0, 50))
        print(x)
        print(start_new_thread(clientsThread, (c, x)))


def clientsThread(c, x):
    count = int(0)
    value = int(0)
    while True:
        data = c.recv(1024)
        if not data:
            break
        if data.decode() == 'Q':
            return
        value = int(data.decode())

        print("Guess" + str(data.decode()))
        if (value == x):
            count += 1
            x1 = "Correct Answer" + str(count)
            c.send(str(x1).encode())
        elif (value < x):
            count += 1
            x1 = "Number is smaller than the guess"
            c.send(str(x1).encode())
        elif (value > x):
            count += 1
            x1 = "Number is bigger than the guess"
            c.send(str(x1).encode())

    c.close()


if __name__ == '__main__':
    Main()
