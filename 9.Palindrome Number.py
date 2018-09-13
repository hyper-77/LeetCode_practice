def PalindromeNumber(n): ## methode by recursion
    if isinstance(n,int):
        if n<0:
            return False
        elif n==0:
            return True
        else:
            div = 1
            temp = n
            while temp > 10:
                temp = temp // 10
                div = div * 10

            print(div)

            return (n//div==n%10) and PalindromeNumber((n-(n//div)*div)//10)



print(PalindromeNumber(19))

##------------------------------------------------------------------------------------------------------------------

def PalindromeNumber2(n): ## methode by loop
    if isinstance(n,int):
        div = 1
        temp = n
        while temp > 10:
            temp = temp // 10
            div = div * 10


        while (n > 0):

            left=n//div
            right=n%10

            if  not left==right: return False
            n=(n%div)//10
            div=div//100


        return True


print(PalindromeNumber2(191))




