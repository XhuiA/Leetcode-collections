#2019.11.18-2
#时间10分钟
#问题分析：需要比较左子树的左、右节点和右子树的右、左节点是否相同，复用原本的树进行比较


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        #复用递归比较
        def summetric(root, cproot):    
            #递归终止条件
            if not root and not cproot:
                return True
            elif not root or not cproot:
                return False
            elif root.val != cproot.val:
                return False
            
            return summetric(root.left, cproot.right) and summetric(root.right, cproot.left)
        
        return summetric(root, root)
