import printmark
import csv


def find(code):
    with open('./barcodes/end.csv') as fileuin:
        listuin = csv.reader(fileuin)
        for row in listuin:
            if row[5] == code:
                print("Ok")
                name = row[2]
                name2 = ""
                if len(name) > 19:
                    name2 = name[19:]
                    name = name[0:19]

                printmark.printmark(name, name2, row[3], row[4], row[1], row[5])


if __name__ == "__main__":
    while True:
        product = find(input())
