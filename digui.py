import sys


def coinChange2( coins :[int], amount :int) -> int:
    a = {amount +1 :amount +1 }

    for i in range(1,amount):
        print(i)


def coinChange( coins :[int],amount :int) -> int:
    memo = dict()
    def dp(n)->int:
        if n in memo : return memo[n]

        if n==0 : return 0
        if n<0 : return -1
        res = sys.maxsize
        for i in coins:
            subp = dp(n-i)
            if subp == -1 : continue
            res = min(res, 1 + subp)
        memo[n] = res if res != sys.maxsize else -1
        return memo[n]
    return dp(amount)

if __name__ == '__main__':
    print(coinChange([1, 2, 5, ], 20))