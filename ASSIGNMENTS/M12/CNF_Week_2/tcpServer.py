import socket
import csv
import threading
from _thread import *


def main():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host1 = socket.gethostname()
    host = socket.gethostbyname(host1)
    port = 5000
    s.bind((host, port))

    s.listen(10)

    myList = []
    rollList = []
    myDict = {}
    with open("data.csv", 'r') as file:
        reader = csv.reader(file)
        for eachRow in reader:
            myList.append(eachRow)
    file.close()

    for rollRida in myList:
        if rollRida[0] not in rollList:
            rollList.append(int(rollRida[0]))
    print(rollList)

    for F2 in myList:
        if F2[0] not in myDict:
            myDict[F2[0]] = F2[1], F2[2]
    print(myDict)

    while not False:
        conn, addr = s.accept()
        dataReceived = conn.recv(1024).decode()
        if dataReceived.split(' ')[0] == "MARK-ATTENDANCE":
            for rollCall in rollList:
                if rollCall not in rollList:
                    message = "ROLLNUMBER-NOTFOUND"
                    conn.send(message.encode())


if __name__ == '__main__':
    main()
