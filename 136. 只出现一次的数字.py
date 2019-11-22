#2019.11.22
#3分钟
#方法：题目要求不使用额外空间且具有线性时间复杂度，所以想知道只出现一次的数，只能用与或方法。
***
交换律：a ^ b ^ c <=> a ^ c ^ b
任何数于0异或为任何数 0 ^ n => n
相同的数异或为0: n ^ n => 0
***

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res = res ^ i
        return res
