#2019.11.22
#时间10分钟
#方法：二叉树的递归


#递归实现
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if(root==None):
            return 0
        else:
            return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
#利用栈的复杂写法
class Solution:
    def getDepth(self, root, depth):
        if not root:
            return depth
        elif not root.left and not root.right:
            return depth+1
        l = self.getDepth(root.left, depth+1)
        r = self.getDepth(root.right, depth+1)
        return max(l, r)
    
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        depth = 0
        depth = self.getDepth(root, depth)
        return depth
