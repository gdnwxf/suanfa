
class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        res = 0
        while True:
            if INT_MAX < res or INT_MIN > res:
                return 0
            ls = x % 10
            if x < 0 and ls > 0:
                ls -= 10
            x =( x-ls) // 10
            if x== 0:
                return res*10+ls
            res = res*10+ls

if __name__ == '__main__':
    print(Solution().reverse(1534236469))