import socket


def main():
    host = '10.10.9.35'
    port = 10020
    s = socket.socket()
    s.connect((host, port))
    msg = input('--> ')
    while msg != 'q':
        s.send(msg.encode())
        data = s.recv(1024)
        print('received from server ' + str(data.decode()))
        msg = input("--> ")
    s.close()


if __name__ == '__main__':
    main()
