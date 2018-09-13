
def longestPalindromicSubstring_dp(s): ## use dynamic programming  running time O(n^2) | space time  O(n^2)
    n=len(s)
    dp = [[0 for x in range(n)] for y in range(n)] ##set the dp table to all zeros D:len(s)*len(s)
    print(dp)
    for i in range(n): ## LPS[i, i]	=	1	Every single character is a palindrome by itself of length 1
        dp[i][i]=1

    print(dp)

    """
    LPS[i, i]	=	1	Every single character is a palindrome by itself of length 1        ## i is start of substr and j is end of substr
    LPS[i, j]	=	2	if j=i+1, sequence has only 2 characters
    LPS[i, j]	=	2 + LPS[i+1, j-1]	If first and last characters are same
    LPS[i, j]	=	MAX(LPS[i+1,j], LPS[i, j-1])	If first and last characters are not same
    """
    ## the way we fill out the dp table , 1.from top left to bottom right fill the diagnal,2. the same way fill the diagnal right to the previos diagnal

    for sublen in range(2,n+1):

        for i in range(0,n+1-sublen):
            j=i+sublen-1
            if s[i]==s[j] and sublen==2: ##LPS[i, j]	=	2	if j=i+1, sequence has only 2 characters

                dp[i][j]=2

            elif s[i]==s[j]:

                dp[i][j]=dp[i+1][j-1]+2  ##LPS[i, j]	=	2 + LPS[i+1, j-1]	If first and last characters are same

            else:

                dp[i][j]=max(dp[i+1][j],dp[i][j-1]) ##LPS[i, j]	=	MAX(LPS[i+1,j], LPS[i, j-1])	If first and last characters are not same

                if dp[i+1][j]>dp[i][j-1]:
                    left=i+1
                    right=j
                else:
                    left=i
                    right=j-1


    print(dp)

    print('Maxlen: '+str(dp[0][n-1]))
    return s[left:right+1]





print(longestPalindromicSubstring_dp('moomn'))



##--------------------------------------------------------------------------------------------------------------------------------

## find lonest Palindrom not by dynamic programming     running time O(n^2)

start = 0
length = 0
def search_palindrom(s,left,right):   #
                                      # word starts at left and end at right s[left:right+1] in order to find the maximum lenth palidrom
    step=1

    global start
    global length

    while (left-step)>=0 and (right+step)<len(s): ## each loop test s[left-1] ?== s[right+1] and if so increment the step, the step is used to calculate the length of the palidrom

        if not s[left-step]==s[right+step]:break

        step+=1


    new_len=right-left+1+2*(step-1)  ## compare to previos maximum palidrom to choose the maximum length palidrom
    if new_len>length:
        length=new_len
        start=left-step+1




def longestPalindromicSubstring(s):
    
    
    global start
    global length

    for i in range(len(s)):
        if i+1<len(s) and s[i]==s[i+1] : # check the base palidrom length==2
            left=i
            right=i+1

            search_palindrom(s,left,right)


        left=i                           #check the base palidrom length==1  (one character)
        right=i

        search_palindrom(s,left,right)



    print(start)
    print('Maxlen: '+str(length))
    print(s[start:length])

longestPalindromicSubstring('moomn')
