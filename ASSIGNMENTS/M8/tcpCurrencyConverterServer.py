import socket
import time


def main():
    dollar = {'INR': 67.0, 'yen': 113.41, 'pound': 0.75}
    INR = {'dollar': 0.014, 'yen': 1.58, 'pound': 0.11}
    pound = {'dollar': 1.26, 'yen': 142, 'INR': 90.0}
    yen = {'dollar': 0.0089, 'INR': 0.63, 'pound': 0.007}
    host = '10.10.9.35'
    lst = [dollar, INR, pound, yen]
    port = 10020
    s = socket.socket()
    s.bind((host, port))
    s.listen(1)
    c, address = s.accept()
    print('connection from ' + str(address))
    while True:
        data = c.recv(1024)
        data = str(data.decode()).split()
        if data[1] == 'dollar':
            result = float(dollar.get(data[4]) * int(data[2]))
        elif data[1] == 'INR':
            result = float(INR.get(data[4]) * int(data[2]))
        elif data[1] == 'yen':
            result = float(yen.get(data[4]) * int(data[2]))
        elif data[1] == 'pound':
            result = float(pound.get(data[4]) * int(data[2]))
        print('sending:' + str(result))
        c.send(str(result).encode())
    c.close()


if __name__ == '__main__':
    main()
