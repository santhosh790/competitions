'''

Given In order and Pre order traversal,

construct the binary tree.
Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal:

[a, b, d, e, c, f, g]

And the following inorder traversal:

[d, b, e, a, f, c, g]

You should return the following tree:

    a
   / \
  b   c
 / \ / \
d  e f  g



'''

#preIndex = 0

class Node:
    def __init__(self, value):
        self.item = value
        self.left = None
        self.right = None

class Node_Operations:

    preIndex = 0

    def travel_inorder(self,node):
            if node == None:
                return
            self.travel_inorder(node.left)
            print(node.item)
            self.travel_inorder(node.right)

    def travel_postoder(self,node):
        if node == None:
            return
        self.travel_postoder(node.left)
        self.travel_postoder(node.right)
        print(node.item)

    def travel_preorder(self, node):
        if node == None:
            return
        print(node.item) # Root node
        self.travel_preorder(node.left) # Left subtree
        self.travel_preorder(node.right) # right subtree


    def find_in_inoder(self, inOrder, rNode, start, end):
        index = 0
        for each in range(start, end):
            if inOrder[each] == rNode:
                index = each
        return index

    def construct_tree(self, inOrder, preOrder, start, end):
        '''
        :param inOrder:
        :param preOrder:
        :param start: Inorder start
        :param end: Inorder end
        :return:

        Logic: Find the first value from preorder and make it root element of the node.
        Find the same value in inorder, it's left part of values will left subtree of root node and right part of nodes
        will right subtree of the root.
        Find next value in the preorder, that will be next left root value below the root node.
        Follow same procedure to create the tree
        '''
        print("Start", start)
        print("end", end)
        ## Inorder start pointer surpasses the Inorder end pointer, completely travelled. Break
        if start > end or self.preIndex > len(preOrder)-1:
            return

        rNode = Node(preOrder[self.preIndex])
        self.preIndex += 1
        print(rNode.item)
        ## The leaf node which has no other values, in InOrder this occurs when start and end are same
        if start == end or end == -1:
            return rNode

        inIndex = self.find_in_inoder(inOrder, rNode.item, start, end)

        rNode.left = self.construct_tree(inOrder, preOrder, start, (inIndex- 1))
        rNode.right = self.construct_tree(inOrder, preOrder, inIndex+1, end)

        return rNode

# Driver program to test above function
inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
preOrder = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
inOrder = ['d', 'b', 'e', 'a', 'f', 'c', 'g']
# Static variable preIndex
#root = buildTree(inOrder, preOrder, 0, 0, len(inOrder)-1)
no = Node_Operations()
no.preIndex = 0
node = no.construct_tree(inOrder,preOrder, 0, len(inOrder)-1)
print(node.item)
print("in order")
no.travel_inorder(node)
print("pre order")
no.travel_preorder(node)