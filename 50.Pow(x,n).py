def Pow(x,n):
    if n==1:
        return x
    elif n<0:
        return 1/Pow(x,-n)
    elif n%2==0:
        temp=Pow(x,n//2)
        return temp*temp
    else:
        temp = Pow(x, n // 2)
        return temp*temp*x




print(Pow(-2,5))