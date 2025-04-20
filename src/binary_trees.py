# binary_tress/py

class TreeNode:
    def __init__(self, val= None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)
        
class BST:
    def __init__(self):
        self.root = None

    def __str__(self):
        return self.inorder_traversal(self.root)
    
    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self._recursive_insert(self.root, val)

    def _recursive_insert(self, root, val):
        if val < root.val:
            if root.left == None:
                root.left = TreeNode(val)
            else:
                self._recursive_insert(root.left, val)
        else:
            if root.right == None:
                root.right = TreeNode(val)
            else:
                self._recursive_insert(root.right, val)

    def inorder_traversal(self, root = None):
        if root is None:
            return ''
        return (self.inorder_traversal(root.left) + f' {root} ' + self.inorder_traversal(root.right)).strip()

    def search(self, val):
        return self._recursive_search(self.root, val)

    def _recursive_search(self, root, val):
        if root is None:
            return False
        elif root.val == val:
            return True
        elif val < root.val:
            return self._recursive_search(root.left, val)
        else:
            return self._recursive_search(root.right, val)
        
    def max(self):
        return self._recursive_max(self.root)
    
    def _recursive_max(self, root):
        if root.right is None:
            return root.val
        else:
            return self._recursive_max(root.right)
    
    def min(self):
        return self._recursive_min(self.root)
    
    def _recursive_min(self, root):
        if root.left is None:
            return root.val
        else:
            return self._recursive_min(root.left)
        
    def delete(self, val):
        # deletes the value if found
        # returns true if found, false if not
        success, _  = self._recursive_delete(self.root, val)
        return success
    
    def _recursive_delete(self, root, val):
        # takes a root note and recursively searches for val
        # if found: deletes it from the tree and returns true
        # else returns false

        if root is None:
            return False, None
        elif val < root.val:
            success, root.left = self._recursive_delete(root.left, val)
            return success, root
        elif val > root.val:
            success, root.right = self._recursive_delete(root.right, val)
            return success, root
        else:
            # in this case val == root.val and we need to delete root
            # we need to replace the root node with the min of the right or the max of the left
            if root.right:
                new_root_val = self._recursive_min(root.right)
                root.val = new_root_val
                success, root.right = self._recursive_delete(root.right, new_root_val)
                return success, root        
            elif root.left:
                new_root_val = self._recursive_max(root.left)
                root.val = new_root_val
                success, root.left = self._recursive_delete(root.left, new_root_val)
                return success, root
            else:
                return True, None


if __name__ == "__main__":
    tree = BST()
    tree.insert(3)
    tree.insert(5)
    tree.insert(19)
    tree.insert(2)
    tree.insert(2)
    tree.insert(-1)
    print('print tree inorder:', tree)
    print("Search for 2, expect true", tree.search(2))
    print("Search for 7, expect false:", tree.search(7))
    print("Find max", tree.max())
    print("Find min", tree.min())
    print('Delete 5:')
    print(tree.delete(5))
    print('print tree inorder:', tree)
    print('Delete 13:')
    print(tree.delete(13))
    print('print tree inorder:', tree)
    
