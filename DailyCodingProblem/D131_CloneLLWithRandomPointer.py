'''
Given the head to a singly linked list, where each node also has a “random” pointer that points to anywhere in the
linked list, deep clone the list.
'''

class Node:
    def __init__(self, data):
        '''
        :param data:
        '''
        self.data = data
        self.next = None
        self.random = None


class RandomLL_Operations:

    def deep_clone(self, head):
        '''
        :param head:
        :return:
        '''

    def create_list(self, node_list, random_list):
        '''
        :param node_list: List of values
        :param random_list: List of random indexes
        :return: head of the list
        '''

        head = Node(node_list[0])
        temp = head
        for each in range(1, len(node_list)):
            node = Node(node_list[each])
            temp.next = node
            temp = temp.next
            #print(node.data)

        temp = head
        for each in range(len(random_list)):
            randIndex = random_list[each]
            randTarget = head
            index = 0
            while randTarget != None:
                if randIndex == index:
                    break
                index += 1
                #print(index)
                randTarget = randTarget.next
            #print("Random %d --> %d"%(temp.data, randTarget.data))
            temp.random = randTarget
            temp = temp.next
        return head

    def print_list(self, head):
        temp = head
        while temp != None:
            print(temp.data)
            print("random next:", temp.random.data)
            temp = temp.next

    def clone_list(self, head):
        '''
        :param head:
        :return:
        '''

        temp = head
        nextEl = head.next

        while nextEl != None:
            newVal = temp.data
            copyNode = Node(newVal)
            copyNode.random = temp.random
            temp.next = copyNode
            copyNode.next = nextEl

            temp = nextEl
            nextEl = nextEl.next

        ## Last element
        lastEl = Node(temp.data)
        lastEl.random = temp.random
        temp.next = lastEl


        temp = head
        new_head = head.next

        while temp.next != None:
            newNode = temp.next
            temp.next = temp.next.next
            temp = newNode

        return new_head

rLLOp = RandomLL_Operations()
head = rLLOp.create_list([1,2,3,4],[1,0,1,3])
rLLOp.print_list(head)
head = rLLOp.clone_list(head)
print("Cloned list")
rLLOp.print_list(head)