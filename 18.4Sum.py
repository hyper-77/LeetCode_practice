def FourSum(array,T): #run time O(n^3)
    array.sort()

    for i in range(len(array)-3):
        for j in range(i+1,len(array)-2):
            left = j + 1
            right = len(array) - 1
            while left < right:
                if array[left] + array[right] == T - array[i]-array[j]:
                    return [array[i],array[j], array[left], array[right]]
                elif array[left] + array[right] < T - array[i]-array[j]:
                    left += 1
                else:
                    right -= 1



    return[-1,-1,-1,-1]




print(FourSum([1,2,3,4,5,6,7,8,9],11))
