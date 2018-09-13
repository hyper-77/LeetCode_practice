def integerToRoman(num):  # num = 1----3999

    v1=["", "M", "MM", "MMM"]

    v2=["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]

    v3=["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]

    v4=["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    return v1[num//1000]+v2[num//100%10]+v3[num//10%10]+v4[num%10]

print(integerToRoman(9))

def RomanToInteger(string):

    m={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    res=0
    for i in range(len(string)):
        val=m[string[i]]
        if i<len(string)-1 and val<m[string[i+1]]: res-=val
        else: res+=val

    return res


print(RomanToInteger(integerToRoman(929)))