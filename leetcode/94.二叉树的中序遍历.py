#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (63.26%)
# Total Accepted:    20K
# Total Submissions: 31.2K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的中序 遍历。
# 
# 示例:
# 
# 输入: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# 输出: [1,3,2]
# 
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        curr = root
        while curr or len(stack):
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        
        return res

# way 2 Morris Traversal -> 线性二叉树
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#         curr = root
#         while curr:
#             if not curr.left:   # 无左子节点处理获取值后直接关联右节点
#                 res.append(curr.val)
#                 curr = curr.right
#             else:   # 有左子节点 -> 保证左子树的右叶节点关联上当前节点
#                 pre = curr.left
#                 while pre.right:
#                     pre = pre.right
#                 pre.right = curr
#                 temp = curr
#                 curr = curr.left
#                 temp.left = None
#         return res

