'''

Given a binary tree, find a minimum path sum from root to a leaf.

For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

  10
 /  \
5    5
 \     \
   2    1
       /
     -1


'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Binary_Ops:

    def construct_tree(self, array):
        root = Node(array[0])
        parent = root
        for each in range(1, len(array)):
            nNode = Node(array[each])
            if parent.left == None:
                parent.left = nNode
            else:
                parent.right = nNode

            if parent.left != None and parent.right != None:
                if root.right.left == None:
                    parent = root.right
                else:
                    parent = parent.left
        return root

    def print_inordertree(self, root):
        if root == None:
            return
        self.print_inordertree(root.left)
        print(root.data)
        self.print_inordertree(root.right)

    def print_preordertree(self, root):
        if root == None:
            return
        print(root.data)
        self.print_preordertree(root.left)
        self.print_preordertree(root.right)

    def min_path(self, root):
        if root == None:
            return 0

        return min(root.data+self.min_path(root.left), root.data+self.min_path(root.right))


bs = Binary_Ops()


root = bs.construct_tree([1,2,3,4])

bs.print_inordertree(root)
bs.print_preordertree(root)

print(bs.min_path(root))




