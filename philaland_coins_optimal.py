
from ast import Not
from msilib.schema import Binary


def noOfCoins(maxPrice):
    binary = format(maxPrice, "b")
    print(len(binary))








test = int(input())
for i in range(test):
    maxPrice = int(input())
    noOfCoins(maxPrice)