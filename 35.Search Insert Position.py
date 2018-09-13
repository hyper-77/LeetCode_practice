def searchInsertPosition(num,T):
    left=0
    right=len(num)
    while(left<right):
        mid=(left+right)//2
        if num[mid]==T: return mid
        elif num[mid]<T: left=mid+1
        else:
            right=mid

    return right


print(searchInsertPosition([1,3,5,7],2))