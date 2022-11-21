print("|x\t|y\t|z\t|f(x,y,z)|")
for x in (True, False):
    for y in (True, False):
        for z in (True, False):
            f = not (x or y or z) == (not x and not y and not z)
            print(f"|{x}\t|{y}\t|{z}\t|{f}\t|")
