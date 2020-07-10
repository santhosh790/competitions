'''

Heap Sort - https://www.programiz.com/dsa/heap-sort
https://www.programiz.com/dsa/heap-data-structure

'''
'''
Heap DS is a complete binary tree that satisfies the heap property. It is also called as Binary heap.

Complete binary tree,
    Every tree node will have left and right nodes filled, except the leaf node's parents.
    
Property of a complete binary tree
    Relationship of a node and it's children:
        Given parent's index is at i, then it's left child will be at index 2i+1 and right child 2i+2.
        So, parent of node i will be (i-1)/2

Heap Property:
    Every children of the node will be lesser in value in max heap. Root will be the highest value in tree. 

Heapify (Max heap):
    root = a[i]
    largest = max(a[i], a[2i+1], a[2i+2])
    if root != largest
        swap(root, largest)

'''

class HeapSort:

    def __init__(self):
        '''
        All operations required for sorting the array
        '''

    def heapify(self, array, size,  i):
        l = (2*i) + 1
        r = (2*i) + 2
        largest = i

        if l < size and array[l] > array[i]:
            largest = l
        if r < size and array[r] > array[largest]:
            largest = r

        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            self.heapify(array, size, largest)
        #return array
        #largest = max(array[i], array[2*i+1], array[2*i+2])

    def heap_sort(self, arr):
        #print((len(array)//2) -1)
        n = len(arr)

        ### Building max heap..
        for i in range((n//2)-1, -1, -1):
            print(i)
            self.heapify(arr, n, i)
        print(arr)

        ## Sorting the elements from back
        for i in range(n-1, 0, -1):
            # Swap
            arr[i], arr[0] = arr[0], arr[i]

            # Heapify root element
            self.heapify(arr, i, 0)



        return arr
hs = HeapSort()
print(hs.heap_sort([2,4,1,3,8,9]))

print(hs.heap_sort([5,4,1,3,8,9]))







'''

List Comprehension
https://www.python-course.eu/list_comprehension.php
image = [[1,1,1],[1,1,0],[1,0,1]]
imageVisited = [[0]*len(image[0])]*len(image)
print(imageVisited)
print(imageVisited[1][1])
print(imageVisited)

imageVist1 = [[None for col in range(cols)] for row in range(rows)]

'''