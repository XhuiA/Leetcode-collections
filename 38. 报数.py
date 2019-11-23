#2019.11.23
#没看明白题目什么意思，索性看了别人的答案

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        else:            
            new_str = ''
            last_str = self.countAndSay(n-1)  # 获取上次的报数
            cur = last_str[0]   # 当前要统计的字符，初始值为last_str的首字符
            cur_t = 0           # 当前字符出现的次数
            
            for i in last_str:
                if i == cur:
                    # 如果相等，则计数+1
                    cur_t += 1
                else:
                    # 否则先报一次数，然后重新初始化开始统计
                    new_str +=str(cur_t) + cur
                    cur = i
                    cur_t = 1
            # 循环结束后，还要再报一次，因为如果最后是以if条件退出循环的，最后几个相同的字符并未报出来
            new_str += str(cur_t) + cur  
            return new_str   
