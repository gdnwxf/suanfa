
if __name__ == '__main__':

    a={"1":212,"2":23111}

    b={"1":50,"3":100}
    bc = b.copy()
    bc.update({k: v for k, v in a.items() if k != '2'})
    print(bc)
    b.update( filter( lambda k:k[0]!='1',a.items()))
    print(b)
    print({ k:v   for k,v in  filter( lambda k
                                      :k[0]!="1",
                                      a.items()) })
    print(list(filter(lambda x:all(x % y != 0 for y in range(2, x)), range(2, 13)))
)