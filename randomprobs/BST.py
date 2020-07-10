'''
Binary Search Tree
'''
class BST_Node:
    def __init__(self, data):

        self.val = data
        self.left = None
        self.right = None


class BST_Ops:

    def construct_tree(self, data, root):
        if root is None:
            root = BST_Node(data)
        elif root.val > data:
            if root.left is not None:
                self.construct_tree(data, root.left)
            else:
                root.left = BST_Node(data)
        else:
            if root.right is not None:
                self.construct_tree(data, root.right)
            else:
                root.right = BST_Node(data)
        return root

    def print_bst_inorder(self, root):
        if root is None:
            return

        self.print_bst_inorder(root.left)
        print(root.val)
        self.print_bst_inorder(root.right)

    def print_bst_preorder(self, root):
        if root is None:
                return
        print(root.val)
        self.print_bst_inorder(root.left)
        self.print_bst_inorder(root.right)

    def print_bst_postorder(self, root):
        if root == None:
                return
        print(root.val)
        self.print_bst_inorder(root.right)
        self.print_bst_inorder(root.left)

    kthelement = 0

    def kth_smallest(self, root, k, nCount):
        if root is None:
            return

        self.kth_smallest(root.left, k, nCount)
        self.kthelement += 1
        nCount[0] += 1
        if self.kthelement == k:
            print("kth::"+str(root.val)+" "+str(nCount[0]))
            return
        self.kth_smallest(root.right, k, nCount)
bs = BST_Ops()
root = None
for each in [8, 4, 7, 3, 2, 5, 1]:
   root = bs.construct_tree(each, root)

print("inorder")
bs.print_bst_inorder(root)
print("preorder")
bs.print_bst_preorder(root)
print("postorder")
bs.print_bst_postorder(root)

print("kth smallest")
nCount = [0]*1
bs.kth_smallest(root, 1, nCount)
print(nCount[0])
bs.kthelement=0
bs.kth_smallest(root, 4, nCount)
