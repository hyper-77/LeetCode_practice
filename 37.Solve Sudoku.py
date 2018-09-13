def isValidSudoku(table,i,j):
   t= table[i][j]
   for row in range(0,9):
       if not(t==0) and(not i==row) and table[row][j]==t:

           return False

   for col in range(0,9):
       if not(t==0) and (not j==col) and table[i][col]==t:

           return False


   for row in range((i//3)*3,(i//3)*3+3):
       for col in range((j // 3) * 3, (j // 3) * 3 + 3):
           if not(t==0) and((not row ==i ) or (not col==j)) and table[row][col]==t:

               return False

   return True





def findNextCelltoFill(table,i,j):
    """for k in range(i,9):
        for v in range(j,9):
            if table[k][v]==0:
                return k,v"""

    for k in range(0, 9):
        for v in range(0, 9):
            if table[k][v] == 0:
                return k, v

    return -1,-1

def solveSudoku(table,i,j):
    if i==9: return True
    if j>=9: return solveSudoku(table,i+1,0)
    if table[i][j]==0:
        for e in range(1,10):
            print(str(i)+':'+str(j)+' '+str(e)+' '+str(isValidSudoku(table,i,j)))
            table[i][j]=e
            if isValidSudoku(table,i,j):
                print(table)
                if(solveSudoku(table,i,j+1)): return True
            else: table[i][j]=0

    else:
        return solveSudoku(table,i,j+1)


    return False


result=[[5, 1, 7, 6, 9, 8, 2, 3, 4], [2, 8, 9, 1, 3, 4, 7, 5, 6], [3, 4, 6, 2, 7, 5, 8, 9, 1], [6, 7, 2, 8, 4, 9, 3, 1, 5], [1, 3, 8, 5, 2, 6, 9, 4, 7], [9, 5, 4, 7, 1, 3, 6, 8, 2], [4, 9, 5, 3, 6, 2, 1, 7, 8], [7, 2, 3, 4, 8, 1, 5, 6, 9], [8, 6, 1, 9, 5, 7, 4, 2, 3]]

input = [[5,1,7,6,0,0,0,3,4],[2,8,9,0,0,4,0,0,0],[3,4,6,2,0,5,0,9,0],[6,0,2,0,0,0,0,1,0],[0,3,8,0,0,6,0,4,7],[0,0,0,0,0,0,0,0,0],[0,9,0,0,0,0,0,7,8],[7,0,3,4,0,0,5,6,0],[0,0,0,0,0,0,0,0,0]]






print(solveSudoku(input,0,0))
print(input)




