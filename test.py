from os import system
if __name__ == "__main__":
    system('clear')
    space = int(input("Length of the board: "))
    space *= space + 1
    f = open('results.txt', 'r').read().split('\n')
    with open('same_shit.txt', 'w') as g:
        for i in range(len(f)//space - 1):
            for j in range(i, len(f)//space):
                if f[i*space] == f[j*space]:
                    for c in range(1, space):
                        if f[i*space+c] != f[j*space+c]:
                            g.write("OH FUCK\n")
                            for c in range(space):
                                g.write(f[i*space+c])
                                g.write('\n')
                            for c in range(space):
                                g.write(f[j*space+c])
                                g.write('\n')
                            pass

