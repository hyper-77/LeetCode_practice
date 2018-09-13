def swap(a,b,list):
    t=list[a]
    list[a]=list[b]
    list[b]=t


def Permutation(start,list,out):

    if start==len(list):
        print(list)
    else:
        for i in range(start,len(list)):
            if (not i==start) and list[i]==list[start]: continue
            swap(start,i,list)
            Permutation(start+1,list,out)
            swap(start,i,list)





Permutation(0,[1,2,1],[])