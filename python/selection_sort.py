def selection_sort(arr):
    for i in  range(len(arr)):
        a =i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[a]:
                a=j
        arr[i],arr[a]=arr[a],arr[i]
num =[1,22,23,45,2,76,677]
print("unsorted numbers",num)
selection_sort(num)
print("Sorted numbers",num)
        