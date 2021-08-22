
def coinChange(coins: [int], amount: int) -> int:
    a = {i: amount+1 for i in range(1, amount+1)}
    # dp[i] = x 表示，当目标金额为 i 时，至少需要 x 枚硬币。
    a[0] = 0
    for i in a:
        for coin in coins:
            if i - coin < 0: continue
            a[i] = min(a[i], 1 + a[i - coin])
    print(a)
    return -1 if a[amount] == amount+1 else a[amount]


if __name__ == '__main__':
    print(coinChange([7, 2, 5 ], 3))

    # 1 2 3 4 5 6 7 8 9 10 11
    # 1 1 2 2 1 2 3 3 3 2 3