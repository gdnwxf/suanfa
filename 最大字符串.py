class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        d =  dict()
        start = end = 0
        ans = 0
        d[s[0]] = 0
        for i, n in enumerate(s[1:]):
            if d.__contains__(n)  :
                dn = d[n]

                #01232
                lf = dn-start
                rt = end -dn
                ans = max(ans, end - start + 1)
                ans = max(ans , max(lf,rt) + 1)

                for k in range(start,dn):
                    del d[s[k]]

                start = dn + 1
            d[n] = i + 1
            end = i + 1
        return  max(ans , end - start+1)

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("dvdf"))
    print(Solution().lengthOfLongestSubstring("abcb"))
    print(Solution().lengthOfLongestSubstring("aa"))
    print(Solution().lengthOfLongestSubstring("au"))
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    print(Solution().lengthOfLongestSubstring("pwwkew"))
    print(Solution().lengthOfLongestSubstring("abba"))
