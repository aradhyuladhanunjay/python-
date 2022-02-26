from statistics import mean
def insertion_sort(array):
    for i in range(1, len(array)):       
        #current number to be compared
        curNum = array [i]
       #compare curNum with the sorted part of the array and insert curNum
        while i>0 and array[i-1] > curNum:
            array[i] = array[i-1]
            i = i-1
            array[i] = curNum
    return array
print(insertion_sort([3,2,1,6,7,4,5]))
print(mean([3,2,1,6,7,4,5]))
