class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class minHeapTree():
    def __init__(self,arr):
        self.root = self.formTree(arr, 0, len(arr))
        
    def formTree(self, arr, left, right):
        if left >= right: return None
        min_val = None; min_index = None
        for i in range(left, right):
            if not min_val or arr[i] < min_val:
                min_val, min_index = arr[i], i
        print(min_val, min_index)
                
        # root
        node = TreeNode(min_val)
        node.left = self.formTree(arr, left, min_index)
        node.right = self.formTree(arr, min_index + 1, right)
        return node
        
    def add(self, x):
        if not self.root:
            self.root = TreeNode(x)
            return
        node = TreeNode(x)
        if x < self.root.val:
            node.left = self.root
            self.root = node
        else:
            prev = self.root; curr = self.root.right
            while curr:
                if curr.val > x:
                    prev.right = node
                    node.left = curr
                    break
                else:
                    prev = curr
                    curr = curr.right
            prev.right = node
    
    def mergeTree(self, newTree):
        root1 = self.root; root2 = newTree.root
        
        def merge(root1, root2):
            if not root1: return root2
            if not root2: return root1
            prev = None; curr = root1
            while curr:
                if root2.val < curr.val:
                    if prev:
                        prev.right = merge(curr, root2)
                        return root1
                    else:
                        root2.left = merge(curr, root2.left)
                        return root2
                else:
                    prev = curr
                    curr = curr.right
            prev.right = root2
            return root1
        
        newroot = merge(root1, root2)
        self.root = newroot
    
    def inorder(self):
        def inordertraversal(node):
            if not node: return []
            return inordertraversal(node.left) + [node.val]  + inordertraversal(node.right)
        return inordertraversal(self.root)
        
    def levelorder(self):
        def bfs(root,level): 
            if len(ans) < level + 1: ans.append([])
            ans[level].append(root.val)
            if root.left: bfs(root.left, level + 1)
            if root.right: bfs(root.right, level + 1)
        ans = []
        if not self.root: return []
        bfs(self.root,0)
        return ans
    
    
def main():
    arr = [6,34,23,21,54,5,46,34,32,23,2,12,2,13,43,435,45,6,5,63,34]
    arr2 = [23,24,15,111]
    tree = minHeapTree(arr)
    tree.add(12)
    tree2 = minHeapTree(arr2)
    tree.mergeTree(tree2)
    print(tree.inorder())
    print(tree.levelorder())
main()
    


