import socket


def main():
    host = '127.0.0.1'
    port = 5000

    server = ('127.0.0.1', 3128)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    message = input("-> ")
    while message != 'q':
        s.sendto(message.encode(), server)
        data = s.recv(1024)
        print("Received from server :" + str(data.decode()))
        message = input("-> ")
    s.close()


if __name__ == '__main__':
    main()
