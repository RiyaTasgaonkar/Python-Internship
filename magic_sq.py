def getsq(n):
    sq= [[0 for x in range(n)]for y in range (n)]
    i=0
    j=n//2
    num=1
    while num  <= n**2 :
        if j > n-1:
            i=i
            j=0
        if i<0:
            i=n-1
            j=j
        if (sq[i][j]!=0):
            i=i-1
            j=j
            continue
        sq[i][j]=num
        num=num+1
        i=i-1
        j=j+1
    for i in sq:
        for j in i:
            print(j,end = ' ')
        print()
n=int(input("Enter value of n"))
print('Magic Square for n = ',n)
getsq(n)
    



