import socket


def main():

    host = '10.10.9.59'
    port = 5000
    dollar = {'INR': 67.0, 'Yen': 113.41, 'Pound': 0.75}
    INR = {'dollar': 0.014, 'Yen': 1.69, 'Pound': 0.011}
    Pound = {'dollar': 1.33, 'INR': 89.3, 'Yen': 151.21}
    Yen = {'dollar': 0.0088, 'INR': 0.59, 'Pound': 0.0066}
    #lis = [dollar, INR, Pound, Yen]
    s = socket.socket()
    s.bind((host, port))
    s.listen(1)
    c, addr = s.accept()
    print("Connection from :" + str(addr))
    while not False:
        data = c.recv(1024)
        data = str(data.decode()).split()
        if data[1] == 'dollar':
            res = float(dollar.get(data[4]) * int(data[2]))
        elif data[1] == 'INR':
            res = float(INR.get(data[4]) * int(data[2]))
        elif data[1] == 'Pound':
            res = float(Pound.get(data[4]) * int(data[2]))
        elif data[1] == 'Yen':
            res = float(Yen.get(data[4]) * int(data[2]))
        print("Sending :" + str(res))
        c.send(str(res).encode())
    c.close()


if __name__ == '__main__':
    main()
