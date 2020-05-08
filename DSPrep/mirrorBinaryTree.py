'''
Given a binary tree, write a function to determine whether the tree is a mirror image of itself. Two trees are a mirror
image if their root values are the same and the left subtree is a mirror image of the right subtree.
'''

class Node:

    def __init__(self, data):
        '''
        :param data:
        '''
        self.data = data
        self.left = None
        self.right = None


class BinaryTree_Operations:

    def mirror_tree(self, head1, head2):
        if head1 == None and head2 == None:
            return True

        if head1 == None or head2 == None:
            return False

        return head1.data == head2.data and self.mirror_tree(head1.left, head2.right)



root1 = Node(1)
root2 = Node(1)

root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

root2.left = Node(3)
root2.right = Node(2)
root2.right.left = Node(5)
root2.right.right = Node(4)

bt = BinaryTree_Operations()
print(bt.mirror_tree(root1, root2))
