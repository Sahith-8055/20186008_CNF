import socket


def main():
    host = '10.10.9.35'
    port = 10023

    server = ('10.10.9.35', 10022)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    message = input("-->")

    while message != 'q':
        s.sendto(message.encode(), server)
        data, addr = s.recvfrom(1024)
        print("Received from Server :" + data.decode())
        message = input("-->")
    s.close()


if __name__ == '__main__':
    main()
