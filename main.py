import numpy as np
import random as r
from os import system
system('clear')


"""cube[z][y][x]"""


# 1 - True (jest kostka) 0 - False (brak kostki) -1 - True (była kostka)
def randomCube(le, n):
    """le - diamerters of cube, n - number of minicubes inside"""
    if le**3 < n:
        print("lo siento amigo mío pero la cagaste")
        return 0
    cube = np.zeros((le, le, le))
    while sum(sum(sum(cube))) < n:
        cube[r.randint(0,le-1)][r.randint(0,le-1)][r.randint(0,le-1)] = 1
    return cube

def repair(cube, le):
    for x in range(le):
        for y in range(le):
            for z in range(le):
                if cube[z][y][x] == -1:
                    cube[z][y][x] = 1

def checkHowManyX(cube, x, y, z, count):
    if cube[z][y][x] != 1:
        return cube, count
    cube[z][y][x] = -1
    count += 1
    
    if y != 0:
        cube, count = checkHowManyX(cube, x, y-1, z, count)
    try:
        cube, count = checkHowManyX(cube, x, y+1, z, count)
    except:
        pass
    if z != 0:
        cube, count = checkHowManyX(cube, x, y, z-1, count)
    try:
        cube, count = checkHowManyX(cube, x, y, z+1, count)
    except:
        pass
    return cube, count


def checkHowManyZ(cube, x, y, z, count):
    if cube[z][y][x] != 1:
        return cube, count
    cube[z][y][x] = -1
    count += 1

    if y != 0:
        cube, count = checkHowManyZ(cube, x, y-1, z, count)
    try:
        cube, count = checkHowManyZ(cube, x, y+1, z, count)
    except:
        pass
    if x != 0:
        cube, count = checkHowManyZ(cube, x-1, y, z, count)
    try:
        cube, count = checkHowManyZ(cube, x+1, y, z, count)
    except:
        pass
    return cube, count

def checkHowManyY(cube, x, y, z, count):
    if cube[z][y][x] != 1:
        return cube, count
    cube[z][y][x] = -1
    count += 1

    if x != 0:
        cube, count = checkHowManyY(cube, x-1, y, z, count)
    try:
        cube, count = checkHowManyY(cube, x+1, y, z, count)
    except:
        pass
    if z != 0:
        cube, count = checkHowManyY(cube, x, y, z-1, count)
    try:
        cube, count = checkHowManyY(cube, x, y, z+1, count)
    except:
        pass
    return cube, count


def giveNumbers(cube, le):
    """cube - 3D cube with minicubes inside, le - diameters of cube"""

    star = []
    for x in range(le):
        ans = []
        for y in range(le):
            for z in range(le):
                if cube[z][y][x] == 1:
                    cube, number = checkHowManyX(cube, x, y, z, 0)
                    ans.append(number)
        star.append(ans)
    repair(cube, le)
    hasht = []
    for y in range(le):
        ans = []
        for z in range(le):
            for x in range(le):
                if cube[z][y][x] == 1:
                    cube, number = checkHowManyY(cube, x, y, z, 0)
                    ans.append(number)
        hasht.append(ans)
    repair(cube, le)
    dick = []
    for z in range(le):
        ans = []
        for x in range(le):
            for y in range(le):
                if cube[z][y][x] == 1:
                    cube, number = checkHowManyZ(cube, x, y, z, 0)
                    ans.append(number)
        dick.append(ans)
    repair(cube, le)
    return (f"axis X: {star} axis Y: {hasht} axis Z: {dick}")




if __name__ == '__main__':

    length = 3
    minicubes = 9

    kostka = randomCube(length, minicubes)
    print(kostka)
    print(giveNumbers(kostka, length))   