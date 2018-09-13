def isMatch(s,p): #implement wildcard matching by recursion
    print('s: '+s)
    print('p: '+p)
    if p=='':return s==''
    if s == '': return p == ''
    if len(p)==1 and len(s)==1:return  (p[0]==s[0] or p[0]=='.')
    if not p[0]=='*':
        return (p[0]==s[0] or p[0]=='.') and isMatch(s[1:],p[1:])
    else:
        while(not s==''):
            if(isMatch(s,p[1:])): return True

            s=s[1:]
        return isMatch(s,p[1:])



print(isMatch('aaa','*aa.'))
