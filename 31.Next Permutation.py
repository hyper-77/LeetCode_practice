def swap(i,j,num):
    t=num[i]
    num[i]=num[j]
    num[j]=t


def nextPermutation(list):
    t=-1
    for i in range(len(list)-1,0,-1):
        if list[i-1]<list[i]:
            t=i-1
            break

    if t == -1:
        list[0:len(list)]=list[len(list)-1::-1]
        return
    print(t)
    min=list[t+1]
    k=t+1
    for j in range(t+1,len(list)):

        if list[j]<min and list[j]>list[t]:

            min=list[j]
            k=j

    swap(k,t,list)

    list[t+1 :] = list[len(list)-1 :t:-1]



num=[1,2,7,4,3,1]

nextPermutation(num)
print(num)

