def removeDuplicates(array):
    pre=0
    cur=0
    while cur<len(array):
        if array[pre]==array[cur]: cur+=1
        else:
            pre+=1
            array[pre]=array[cur]
            cur+=1

    return pre+1


print(removeDuplicates([1,1,2,2,3,3,3,4,5,6,7,7,7]))