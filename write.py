import numpy as np
from main import randomCube, giveNumbers


def writeItDown(le, n, rep):
    with open("results.txt", 'w') as f:
        for i in range(rep):
            kostka = randomCube(le, n)
            ax = giveNumbers(kostka, le)
            f.write(ax +'\n'+ str(kostka)+ '\n')

if __name__ == "__main__":
    try:
        le = int(input("Length of the board: "))
        minicubes = int(input("Number of minicubes: "))
        repeats = int(input("Number of results: "))
    except:
        print("lo siento amigo mío pero la cagaste")
    else:
        writeItDown(le, minicubes, repeats)