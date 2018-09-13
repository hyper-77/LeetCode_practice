def ThreeSum(array,T):
    array.sort()

    for i in range(len(array)-2):
        left=i+1
        right=len(array)-1
        while left<right:
            if array[left]+array[right]==T-array[i]: return [array[i],array[left],array[right]]
            elif array[left]+array[right]<T-array[i]: left+=1
            else: right-=1


    return[-1,-1,-1]




print(ThreeSum([1,2,3,4,5,6,7,8,9],10))
