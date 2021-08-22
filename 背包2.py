

def pak( s,wt ,val, i , N, W):
    global mx
    tmx = sum([val[i] for i in s])
    if tmx > mx:
        global rst
        rst = s.copy()
        mx = tmx
    for k in range(i,N):
        if wt[k] <= W:
            s.append(k)
            pak(s,wt,val,k+1,N , W-wt[k] )
            s.remove(k)

if __name__ == '__main__':
    # 前N个物品  背包W 容量
    N = 4; W = 7
    wt = [2, 1, 3, 4]
    val = [4, 2, 3, 9]


    # dp[N][W] 第前N个物品在最大重量为W的时候的最大价值

    mx= 0
    sm = 6
    s  =[]
    rst = []
    for i in range(0,N):
        if wt[i] == W:
            mx = max(mx, val[i])
            rst = [i]
            continue
        elif  wt[i] < W :
            s.append(i)
            pak(s,wt,val,i+1,N,W-wt[i] )
            s.remove(i)
        else:
            continue



    #print(dp[N][W])
    print(mx)
    print(rst)
