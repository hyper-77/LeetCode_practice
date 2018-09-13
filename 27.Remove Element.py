def removeElement(num,T):
    res=0

    for i in range(len(num)):
        if not num[i]==T:
            num[res]=num[i]
            res+=1

    return res

num=[1,2,3,3,3,3,5,7,3]
print(removeElement(num,3))
print(num)