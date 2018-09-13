def generate_parenthese(s,start,end,n):
    if end==n and start==end:
        print(s)


    if start<end:
        generate_parenthese(s+')', start+1, end, n)

    if end<n:
        generate_parenthese(s+'(', start, end+1, n)






generate_parenthese('',0,0,3)