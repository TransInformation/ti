import copy

class Sort:
    
    def invoke(self, arr):
        raise NotImplementedError("The method must be realized.")

    def __call__(self, arr):
        return self.invoke(arr)


class QuickSort(Sort):

    def invoke(self, arr):
        if arr == []: 
            return []
        else:
            pivot = arr[0]
            lesser = self.invoke([x for x in arr[1:] if x < pivot])
            greater = self.invoke([x for x in arr[1:] if x >= pivot])
        lesser = lesser if lesser is not None else []
        pivot = [pivot] if [pivot] is not None else []
        greater = greater if greater is not None else []
        a = lesser + pivot + greater
        return a
        
#__________________________________________________
class MergeSort(Sort):

    
    @staticmethod
    def merge(left, right):
        result = []
        i ,j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result
    
    def invoke(self, arr):
        array = copy.copy(arr)
        if len(array) < 2:
            return array
        middle = len(array) //2
        left = self.invoke(array[:middle])
        right = self.invoke(array[middle:])
        return self.merge(left, right)

#__________________________________________________

class BubbleSort(Sort):

    def invoke(self, array):
        arr = copy.copy(array)
        for i in range(len(arr)-1):
            for j in range(len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    buff = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = buff
        return arr
#__________________________________________________
class SelectSort(Sort):

    def invoke(self, arr):
        array = copy.copy(arr)
        for i in range(len(array) - 1):
            m = i
            j = i + 1
            while j < len(array):
                if array[j] < array[m]:
                    m = j
                j = j + 1
            array[i], array[m] = array[m], array[i]
        return array




