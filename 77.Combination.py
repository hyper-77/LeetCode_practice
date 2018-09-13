def Combination(start,stop,n,k,out):
    if stop>=k:
        print(out)
    else:
        for i in range(start,n+1):
            out.append(i)
            Combination(i+1,stop+1,n,k,out)
            out.pop()


Combination(1,0,5,3,[])