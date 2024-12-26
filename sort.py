num =[1,2,3,4,5,99,1001]
numbers_list=sorted(num)
reverse_list=sorted(num, reverse=True)
if numbers_list ==sorted(num):
    print("The list of numbers are arranged in ascending order:",numbers_list)
elif numbers_list==reverse_list:
    print("The list of numbers are arranged in descending order:",reverse_list)
else:
    print("The numbers are not sorted:")