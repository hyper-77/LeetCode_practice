n=5
print(n)


C=[0 for i in range(int(n)+1)]
C[0]=1
C[1]=1

for i in range(2,n+1):
    for j in range(0,i):
        C[i]+=C[j]*C[i-j-1]

print(C)
