def isValidSudoku(table):
    rowCheck=[]
    colCheck=[]
    cellCheck=[]
    for i in range(9):
        rowCheck.append([])
        colCheck.append([])
        cellCheck.append([])


    for row in range(len(table)):

        for col in range(len(table[row])):

            c=table[row][col]
            if c==0:
                continue
            elif c<1 or c>9:
                return False
            else:
                if c in rowCheck[row]:

                    return False
                elif c in colCheck[col]:

                    return False
                elif c in cellCheck[3*(int(row /3)) + int(col / 3)]:


                    return False
                else:
                    rowCheck[row].append(c)
                    colCheck[col].append(c)
                    cellCheck[3*(int(row /3)) + int(col / 3)].append(c)

    return True


table=[[5, 1, 7, 6, 9, 8, 2, 3, 4], [2, 8, 9, 1, 3, 4, 7, 5, 6], [3, 4, 6, 2, 7, 5, 8, 9, 1], [6, 7, 2, 8, 4, 9, 3, 1, 5], [1, 3, 8, 5, 2, 6, 9, 4, 7], [9, 5, 4, 7, 1, 3, 6, 8, 2], [4, 9, 5, 3, 6, 2, 1, 7, 8], [7, 2, 3, 4, 8, 1, 5, 6, 9], [8, 6, 1, 9, 5, 7, 4, 2, 3]]

input = [[5,1,7,6,0,0,0,3,4],[2,8,9,0,0,4,0,0,0],[3,4,6,2,0,5,0,9,0],[6,0,2,0,0,0,0,1,0],[0,3,8,0,0,6,0,4,7],[0,0,0,0,0,0,0,0,0],[0,9,0,0,0,0,0,7,8],[7,0,3,4,0,0,5,6,0],[0,0,0,0,0,0,0,0,0]]

print(isValidSudoku(input))


