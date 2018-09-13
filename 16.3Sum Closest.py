def ThreeSumClosest(array,T):
    array.sort()
    dif=abs(array[0]+array[1]+array[2]-T)

    for i in range(len(array)-2):
        left=i+1
        right=len(array)-1
        while left<right:
            if abs(array[left]+array[right]+array[i]-T)<dif:
                dif=abs(array[left]+array[right]+array[i]-T)
                sum=array[left]+array[right]+array[i]
            if array[left]+array[right]<T-array[i]: left+=1
            else: right-=1


    return[sum,dif]




print(ThreeSumClosest([1,2,3,4,5,6,7,8,9],25))
