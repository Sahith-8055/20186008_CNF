import csv

if __name__ == '__main__':
    with open("data.csv", 'r') as file:
       reader = csv.reader(file)
       for eachRow in reader:
           print(eachRow)
    file.close()