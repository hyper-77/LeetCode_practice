def longestCommonPrefix(array):
    res=''
    for i in range(len(array[0])):
        c=array[0][i]
        for j in range(1,len(array)):
            if i >=len(array[j]) or not array[j][i]==c:return res

        res+=c

    return res


print(longestCommonPrefix(['abc','abq','a']))


