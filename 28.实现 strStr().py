#2019.11.23
#方法一：时间5分钟；kmp算法：10分钟
#方法分析：字符串匹配问题，暴力匹配方法和kmp算法。
#注意需要加强kmp算法的写的速度，这种简单题应该就是普通匹配方法。

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #普通匹配方法
        if needle == '':
            return 0
        if needle not in haystack:
            return -1
        else:
            for i in range(len(haystack)):
                if haystack[i] == needle[0]:
                    if haystack[i:i+len(needle)] == needle:
                        return i 
                        

   #KMP算法
   #第一步：生成needle的部分匹配表
   #第二步：使用匹配表对haystack进行匹配
class Solution:
    def strStr(self, t, p):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not p : return 0
        _next = [0] * len(p)

        def getNext(p, _next):
            _next[0] = -1
            i = 0
            j = -1
            while i < len(p) - 1:
                if j == -1 or p[i] == p[j]:
                    i += 1
                    j += 1
                    _next[i] = j
                else:
                    j = _next[j]
                    
        getNext(p, _next)
        i = 0
        j = 0
        while i < len(t) and j < len(p):
            if j == -1 or t[i] == p[j]:
                i += 1
                j += 1
            else:
                j = _next[j]
        if j == len(p):
            return i - j
        return -1
       
