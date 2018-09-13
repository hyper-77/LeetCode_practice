def SearchRange(list,T):
    tmp=[-1,-1]
    left=0
    right=len(list)
    while(left<right):
        mid=(left+right)//2
        if list[mid]<T:
            left=mid+1
        else:
            right=mid


    if (list[right]==T):
        tmp[0]=right
    left = 0
    right = len(list)
    while (left < right):
        mid = (left + right) // 2
        if list[mid] <= T:
            left = mid + 1
        else:
            right = mid


    if (list[right-1] == T):
        tmp[1] = right-1


    return tmp







print(SearchRange([5, 7, 7, 8, 8, 10] ,0))