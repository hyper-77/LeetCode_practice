def containWithMostWater(array):
    left=0
    right=len(array)-1
    maxVol=0
    while left<=right:
        vol=(right-left+1)*min(array[left],array[right])
        if vol>maxVol:
            maxVol=vol
        if array[left]<array[right]:
            left+=1
        else:
            right-=1

    return maxVol


print(containWithMostWater([5,3,15,20,3,3]))