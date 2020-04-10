class Solution:
    def reverseWords(self, s: str) -> str:
        # 直接暴力来了
        if len(s) == 0:
            return s
        end = len(s)
        rep = []
        r = len(s) - 1
        # token 遍历
        while r >= 0:
            # 先过滤下空的
            while r >= 0 and s[r] == ' ':
                r -= 1
            if r < 0:
                break
            
            # 当前s[r]肯定不是空
            next_r = r - 1
            while next_r >= 0 and s[next_r] != ' ':
                next_r -= 1

            # 1个字符的话，next_r就会变成-1，r=0
            # token 结束
            # r这个位置是有字符的，next_r是么得的
            token = s[next_r + 1:r + 1]
            rep.append(token)
            r = next_r
        return ' '.join(rep)
