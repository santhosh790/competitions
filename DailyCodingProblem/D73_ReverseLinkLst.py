'''

Given the head of a singly linked list, reverse it in-place
'''

class SLItem:
    def __init__(self, val):
        self.item = val
        self.next = None


class SL_Operations:

    def add_item(self, item, tail):
        lastElement = SLItem(item)
        tail.next = lastElement

    def create_linked_list(self, itemList):
        if len(itemList) == 0:
            return None
        head = SLItem(itemList[0])
        temp = head
        for each in range(1, len(itemList)):
            slItem = SLItem(itemList[each])
            temp.next = slItem
            temp = slItem
        return head


    def reverse_list(self, head):
        if (head == None or head.next == None):
             return head

        nextEl = head.next
        head.next = None

        while nextEl != None:
            temp = nextEl
            nextEl = nextEl.next

            temp.next = head
            head = temp
        return head

    def reverse_recur(self, head):
        '''

        :param head:
        :return:
        Go till last element and return that as head of the item and
        from next element (el) onwards,
        make it's next element's pointer (el+1) to point it (el) and make el to point nothing
        '''
        if (head == None or head.next == None):
            print("in con", head.item)
            return head
        print(head.item)
        head_rev = self.reverse_recur(head.next)
        print("head rev", head_rev.item, head.item)

        head.next.next = head
        head.next = None
        return head_rev

    def display(self, head):
        while head != None:
            print(head.item)
            head = head.next

sl = SL_Operations()
list_head = sl.create_linked_list([7, 14, 21, 28])
print(list_head)
print("Original: ",end="")
sl.display(list_head)
#list_head = sl.reverse_list(list_head)
list_head = sl.reverse_recur(list_head)
print("After Reverse: ", end="")
sl.display(list_head)