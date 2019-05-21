#Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).#

class binary(object):
    def Node(self,x):
        self.val=x
        self.left=None
        self.right=None
        
    def rangeSumBST(self, root, L, R):
        ans=0
        s=[root]
        while s:
            node=s.pop()
            if node:
                if L<=node.val<=R:
                    ans+=node.val
                if node.val<L:
                    s.append(node.val)
                if node.val>R:
                    s.append(node.val)
        return ans
        
root = Node(10) 
root.left = Node(7) 
root.right = Node(15) 
root.left.right = Node(5) 
root.left.left = Node(3) 
root.right.right = Node(18) 

numbers=binary()
answer=rangeSumBST(root, L, R)
