def BinarySearch(num,T):
    left=0
    right=len(num)
    while left<right:
        mid=int((left+right)/2)
        if num[mid]==T:
            return mid
        elif num[mid]<T:
            left=mid+1
        else:
            right=mid

    return -1


print(BinarySearch([1,2,3,6,8,10],10))


def BinarySearch_low_bound(num,T): ##查找最后一个小于目标值的数
    left=0
    right=len(num)
    while left<right:
        mid=int((left+right)/2)
        if num[mid]<T:
            left=mid+1
        else:
            right=mid

    return right-1

print(BinarySearch_low_bound([1,2,3,6,8,10],7))