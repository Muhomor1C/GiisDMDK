import printmark
import csv


def find(code):
    with open('./barcodes/end.csv') as fileuin:
        listuin = csv.reader(fileuin)
        for row in listuin:
            if row[5] == code:
                print()
                printmark.printmark(row[2], row[3], row[4], row[1], row[5])


if __name__ == "__main__":
    while True:
        product = find(input())
