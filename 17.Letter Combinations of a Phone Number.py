import copy
def letterCombination(num): # solve this by iterative
    m={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    res=['']
    for char in num:
        temp=copy.deepcopy(res)
        res=[]
        for element in temp:
            for letter in m[char]:
                res.append(element+letter)

    return res

print(letterCombination('23'))


out=[] # solve by recursion
m={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
def letterCombination_recur(num,start,res,out):

    if start>=len(num):
        out.append(copy.deepcopy(res))

    else:
        for char in m[num[start]]:
            res+=char
            letterCombination_recur(num,start+1,res,out)
            res=res[:-1]


letterCombination_recur('23',0,'',out)
print(out)


