def check(a, i, j):
    for n in range(i):
        if a[n][j] == 1:
            return False

    for n in range(j):
        if a[i][n] == 1:
            return False

    l = i - 1
    r = j - 1
    while l >= 0 and r >= 0:
        if a[l][r] == 1:
            return False
        l -= 1
        r -= 1

    # l = i + 1
    # r = j + 1
    # while l < 8 and r < 8:
    #     if a[l][r] == 1:
    #         return False
    #     l += 1
    #     r += 1

    # l = i + 1
    # r = j - 1
    # while l < 8 and r >= 0:
    #     if a[l][r] == 1:
    #         return False
    #     l += 1
    #     r -= 1

    l = i - 1
    r = j + 1
    while l >= 0 and r < 8:
        if a[l][r] == 1:
            return False
        l -= 1
        r += 1

    return True


def printArr(a):
    print("\n".join([str(i) for i in a]))



def find_q(t,i):
    if i > 7:
        global cc
        cc+=1
        printArr(t)
        print(" ========== ")
        return
    for j in range(0, 8):
        if check(t, i, j):
            t[i][j] = 1
            find_q(t,i+1)
            t[i][j] = 0

if __name__ == '__main__':

    cc=0
    a = [[0 for i in range(8)] for j in range(8)]
    t = a.copy()
    find_q(t,0)

    print(cc)


    printArr(a)
