def canEat(piles, s , H):
    t = 0
    for i in piles:
        t+= int(i / s)  + 1 if i%s != 0 else i/s
        if t>H:
            return False
    return True

if __name__ == '__main__':
    piles=[3,6,7,11] ; H=8
    piles = [30,11,23,4,20] ; H=5
    a = max(piles)
    mi = 1
    for i in range(1,a+1):
        if canEat(piles,i,H):
            mi = i
            break
    print(mi)