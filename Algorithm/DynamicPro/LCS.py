#Longest Common Subsequence
def LCS(X,Y):
    m=len(X)
    n=len(Y)
    c=[[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1]==Y[j-1]:
                c[i][j]=c[i-1][j-1]+1
            elif c[i-1][j]>=c[i][j-1]:
                c[i][j]=c[i-1][j]
            else:
                c[i][j]=c[i][j-1]
    return c
'''
space complexity:O(min(m,n))+O(1)
c[i,j] is determined by c[i-1,j-1],c[i-1,j] and c[i,j-1]
use A to store A[i-1][j-1] and left is c[i-1], up is c[i]
'''
def LCS_Length(X,Y):
    m=len(X)
    n=len(Y)
    if n>=m:
        c=[0 for i in range(m+1)]
        for j in range(1,n+1):
            A=0
            for i in range(1,m+1):
                if X[i-1]==Y[j-1]:
                    c[i]=A+1
                elif c[i-1]>c[i]:
                    c[i]=c[i-1]
                A=c[i]
        return c[m]
    else:
        c=[0 for j in range(n+1)]
        for i in range(1,m+1):
            A=0
            for j in range(1,n+1):
                if X[i-1]==Y[j-1]:
                    c[j]=A+1
                elif c[j-1]>c[j]:
                    c[j]=c[j-1]
                A=c[j]
        return c[n]
def Draw_LCS(c,X,i,j):
    if i==0 or j==0:
        return
    if c[i][j]==c[i-1][j-1]+1:
        Draw_LCS(c,X,i-1,j-1)
        print(X[i-1])
    elif c[i][j]==c[i-1][j]:
        Draw_LCS(c,X,i-1,j)
    else:
        Draw_LCS(c,X,i,j-1)
        
X=['A','T']
Y=['A','T','T','C','G','T','C']
c=LCS(X,Y)
Draw_LCS(c,X,len(X),len(Y))
