



if __name__ == '__main__':
    a  = [1,8,6,2,5,4,8,3,7]
    i = 0
    j = len(a) -1
    rst = 0
    while i < j:
        rst = max(((j-i) * min(a[i],a[j])),rst)
        if a[j]> a[i]:
            i += 1
        else:
            j -= 1

    print(rst)