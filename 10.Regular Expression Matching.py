def isMatch(s,p):  #Regular Expression by using recursion
    print('s: '+s)
    print('p: '+p)

    if p=='': return s==''   #base case: if s and p is empty recursion will end
    if  len(p)==1 :          #base case: if  s and p is one character recursion will end
        return len(s)==1 and(s[0]==p[0] or p[0]=='.')


    if not p[1]=='*':                          # when second charactor of p is not *
        return (s[0]==p[0] or p[0]=='.') and isMatch(s[1:],p[1:])

    else:                                      # when second charactor of p is *
        while(not s=='') and (s[0]==p[0] or p[0]=='.'):  # suppose s=aaaabc p=a*bc
                                                         # 1st loop isMach(aaaabc,bc) ,2nd isMatch(aaabc,bc),3.isMatch(aabc,bc),4.isMatch(abc,bc)
            if isMatch(s,p[2:]): return True
            s=s[1:]

        return isMatch(s,p[2:])    # isMatch(bc,bc)


print(isMatch('aa','.*a'))


def isMatch_dp(s,p): #solve by dynamic programming
    dp = [[False for x in range(len(p)+1)] for y in range(len(s)+1)]
    dp[0][0]=True
    print(dp)
    for i in range(1,len(s)+1):
        for j in range(1,len(p)+1):
            if j>1 and p[j-1]=='*':
                print('@@@@@')
                print(dp[i][j-2] )
                dp[i][j]=dp[i][j-2] or ((p[j-2]==s[i-1] or p[j-2]=='.') and dp[i-1][j])
            else:
                dp[i][j]=(s[i-1]==p[j-1]or p[j-1]=='.')and dp[i-1][j-1]

    print(dp)

isMatch_dp('aa','.*a')

