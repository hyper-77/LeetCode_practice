def solveNQ(table,i,n):
    if i==n:
        for k in range(n):
            string=""
            for t in range(n):
                string+=str(table[k][t])
            print(string)
        print('-----------------------------------------')
    else:
        for col in range(0,n):

            if (isValidNQ(table,i,col)):
                table[i][col] = 1
                solveNQ(table,i+1,n)
                table[i][col] = 0








def isValidNQ(table, row,col):
    for i in range(row):
        if table[i][col]==1:
            return False

    i=row-1
    j=col-1
    while i>=0 and j>=0:
        if table[i][j]==1:
            return False

        i-=1
        j-=1


    i=row-1
    j=col+1
    while i>=0 and j<len(table):
        if table[i][j]==1:
            return False
        i-=1
        j+=1



    return True





input=[]
for i in range(8):
    temp=[]
    for j in range(8):
        if j==100:
            temp.append(1)
        else:
            temp.append(0)

    input.append(temp)


print(input)
print(isValidNQ(input,7,7))
solveNQ(input,0,8)



