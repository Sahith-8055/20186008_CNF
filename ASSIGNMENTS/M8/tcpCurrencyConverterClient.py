import socket


def main():

    host = '10.10.9.59'
    port = 3129

    s = socket.socket()
    s.connect((host, port))

    message = input("->")
    while message != 'q':
        s.send(message.encode())
        data = s.recv(1024)
        print("Received the output :" + str(data.decode()))
        message = input("->")
    s.close()


if __name__ == '__main__':
        main()
