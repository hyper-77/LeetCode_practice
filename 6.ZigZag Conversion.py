def ZigZag(s,n):
    l=2*n-2
    table = [[] for y in range(n)]
    print(table)
    for i in range(len(s)):
        if (i%l)>=0 and (i%l)<=n-1:
            table[i%l].append(s[i])
        else:
            table[l-(i%l)].append(s[i])

    string=''
    for k in table:
        for v in k:
            string+=v

    print(table)
    return string







print(ZigZag('0123456789ABCDEF',4))