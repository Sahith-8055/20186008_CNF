import socket


def main():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host1 = socket.gethostname()
    host = socket.gethostbyname(host1)
    port = 5000

    connectionList = []
    s.bind((host, port))
    s.listen(10)
    while not False:
        conn, addr = s.accept()
        print("Connection from :" + str(addr))
        connectionList.append(addr)
        data = conn.recv(1024).decode()
        if not data:
            break
        print("From connected user: " + str(data))
