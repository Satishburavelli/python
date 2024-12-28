def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:arr[j],arr[j+1]=arr[j+1],arr[j]
num =[2,4,54,64,12,3]
print('the unsorted numbers',num)
bubble_sort(num)
print("The sorted numbers",num)
        