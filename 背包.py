

if __name__ == '__main__':
    # 前N个物品  背包W 容量
    N = 4;
    W = 7
    wt = [2, 1, 3, 4]
    val = [4, 2, 3, 9]
    dp = [[0 for j in range(W+1)]  for i in range(N+1)]

    # dp[N][W] 第前N个物品在最大重量为W的时候的最大价值

    for i in range(1,N+1):
        for w in range(1,W+1):

            #dp[i][w] = dp[i-1][w - wt[i-1]]+val[i]

            if  w - wt[i - 1] < 0 :
            # 当前背包容量装不下，只能选择不装入背包
                dp[i][w] = dp[i - 1][w]
            else:
                # 装入或者不装入背包，择优
                dp[i][w] = max(dp[i - 1][w - wt[i-1]] + val[i-1], dp[i-1][w])
            print(i ,w , dp[i][w])

    print(dp[N][W])
