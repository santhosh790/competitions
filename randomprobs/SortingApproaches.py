'''

Practicing every sorting algorithms
1. Bubble Sort
2. Insertion Sort
3. Merge Sort
4. Quick Sort

'''


class SortArray:

    def bubble_sort(self, array):
        '''
        :param array:
        :return: array

        This algorithm works by replacing the values from neighboring element.
        In one iteration, the max value goes at the end. So second iteration will go till end-1

        To optimize this, we can have a flag to check if it s going into the if condition, if not going,
        it means the array is already sorted, so we can break
        '''

        for i in range(len(array)-1):
            for j in range(len(array)-i-1):
                if array[j] > array[j+1]:
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp
            print(array)
        return array

    def insertion_sort(self, array):
        '''
        :param array: unsorted values
        :return: array: sorted values
        It takes the value key from the outer loop position i,
        in inner loop, start from i-1th position, move element one step front until the element is smaller than previous

        It is like finding the correct position of the element key and inserting at that position.
        '''
        for i in range(1, len(array)):
            key = array[i]
            j = i-1
            while j>=0 and array[j] > key:
                array[j+1] = array[j]
                j = j-1
            array[j+1] = key # even when while loop not executed (j+1) is actually i. So, nothing changes
            print(array)
        return array

    def merge_sort(self, array):
        '''
        :param array: unsorted array
        :return: array: sorted array

        It works by Divide and Conquer approach. Divide the array into two halves recursively
        until it becomes 1 element array.
        Then merge those two arrays by checking whether left is greater than right

        '''
        if len(array) > 1: ## Dividing condition
            m = len(array)//2
            left = array[:m]
            right = array[m:]

            self.merge_sort(left)
            self.merge_sort(right)

            i=j=k=0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    array[k] = left[i]
                    k += 1
                    i += 1
                else:
                    array[k] = right[j]
                    k += 1
                    j += 1
            ## for left out in both left and right

            while i < len(left):
                array[k] = left[i]
                k += 1
                i += 1

            while j < len(right):
                array[k] = right[j]
                k += 1
                j += 1
        print(array)
        return array

    def partition(self, array, low, high):
        pivVal = array[high]
        i = low
        for j in range(low, high):
            if array[j] < pivVal:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
                i = i+1
        array[i], array[high] = array[high], array[i]
        return i

    def quick_sort(self, array, low, high):
        '''
        :param array: unsorted array
        :return: array: sorted array
        It is a Divide and conquer algorithm.
        Pick a pivot point element, Then split array in a way that all elements lesser than pivot is left of pivot and
        greater than pivot to right of the pivot element.
        Keep sorting in this way till left and right collides.
        Now the elements will be completely sorted.
        '''
        if low < high:
            pivot = self.partition(array, low, high)
            self.quick_sort(array, low, pivot-1)
            self.quick_sort(array, pivot+1, high)
        return array



sor = SortArray()
array = [9,8,10,4,1]
print('bubble sort')
print(sor.bubble_sort([3,4,5,4,1]))
print('insertion sort')
#print(sor.insertion_sort(array))
print('merge sort')
print(array)
#print(sor.merge_sort(array))
print(sor.quick_sort(array, 0, len(array)-1))