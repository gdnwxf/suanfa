def canEat(piles, s , H):
    t = 0
    for i in piles:
        t+= int(i / s)  + 1 if i%s != 0 else i/s
        if t>H:
            return False
    return True

if __name__ == '__main__':
    piles=[3,6,7,11] ; H=8
    #piles = [30,11,23,4,20] ; H=5
    l=1; r = max(piles) + 1
    while l < r:
        mid =int((r-l)/2) + l
        if canEat(piles,mid,H):
            r = mid
        else:
            l =mid +1
    print(l)