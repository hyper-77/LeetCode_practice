import copy
result=[]
count=0
def CombinationSum(start,target,out,list): ##select all possible of numbers from the set that sum up to value of target(and the same number can be used many times)
    if target<0:
        return
    elif target==0:


        a=copy.deepcopy(out)
        result.append(a)

    else:

        for i in range(start,len(list)):
            out.append(list[i])
            CombinationSum(i, target-list[i], out, list)
            out.pop()




CombinationSum(0,7,[],[2,3,5,7])
print(result)

result=[]
def CombinationSum3(start,target,out,list,k): ## select k numumbers from the set that sum up to value of target
    if k<0:
        return
    elif target<0:
        return
    elif target==0 and k==0:
        a=copy.deepcopy(out)
        result.append(a)
    else:
        for i in range(start,len(list)):
            out.append(list[i])
            CombinationSum3(i,target-list[i],out,list,k-1)
            out.pop()


CombinationSum3(0,7,[],[2,3,5,7,4],2)
print(result)