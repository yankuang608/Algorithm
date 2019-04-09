#Strassen's algorithm for matrix multiplication time Complexity o(n^2.81)
import random
width=8
A=[random.sample(range(10),width) for x in range(width)]
B=[random.sample(range(10),width) for x in range(width)]
def Matrix_Add(A,B):
    n=len(A)
    R=[[ 0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            R[i][j]=A[i][j]+B[i][j]
    return(R)

def Matrix_Sub(A,B):
    n=len(A)
    R=[[ 0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            R[i][j]=A[i][j]-B[i][j]
    return(R)        

def Partition(A): #partition into A_11,A_12,A_21,A_22
    n=len(A)
    mid=(n//2)-1
    A_11=[[0 for x in range(mid+1)]for y in range(mid+1)]
    A_12=[[0 for x in range(mid+1,n)]for y in range(0,mid+1)]
    A_21=[[0 for x in range(0,mid+1)]for y in range(mid+1,n)]
    A_22=[[0 for x in range(mid+1,n)]for y in range(mid+1,n)]
    for i in range(0,mid+1):
        for j in range(0,mid+1):
                A_11[i][j]=A[i][j]
    for i in range(0,mid+1):
        for j in range(0,n-mid-1):
                A_12[i][j]=A[i][mid+1+j]
    for i in range(0,n-mid-1):
        for j in range(0,mid+1):
                A_21[i][j]=A[mid+1+i][j]
    for i in range(0,n-mid-1):
        for j in range(0,n-mid-1):
                A_22[i][j]=A[mid+1+i][mid+1+j]
            
    return(A_11,A_12,A_21,A_22)

def Combine(A_11,A_12,A_21,A_22):#the reverse process of Partition()
    mid=len(A_11)-1
    n=len(A_11)+len(A_21)
    A=[[0 for x in range(n)] for y in range(n)]
    
    for i in range(0,mid+1):
        for j in range(0,mid+1):
            A[i][j]=A_11[i][j]
    for i in range(0,mid+1):
        for j in range(0,n-mid-1):
            A[i][mid+1+j]=A_12[i][j]
    for i in range(0,n-mid-1):
        for j in range(0,mid+1):
            A[mid+1+i][j]=A_21[i][j]
    for i in range(0,n-mid-1):
        for j in range(0,n-mid-1):
            A[mid+1+i][mid+1+j]=A_22[i][j]
            
    return(A)
    
    

def Matrix_Multiply(A,B):
    n=len(A)
    C=[[0 for x in range(n)] for y in range(n)]
    if n==1:
        C[0][0]=A[0][0]*B[0][0]
    else:
        #step 1 Partition
        mid=n//2
        A_11=[[0 for x in range(mid)] for y in range(mid)]
        A_12=A_21=A_22=B_11=B_12=B_21=B_22=C_11=C_12=C_21=C_22=A_11
        A_11,A_12,A_21,A_22=Partition(A)
        B_11,B_12,B_21,B_22=Partition(B)
        C_11,C_12,C_21,C_22=Partition(C)
        #step 2 Create 10 matrix S_1...S_10 by Add or Sub
        S_1=Matrix_Sub(B_12,B_22)
        S_2=Matrix_Add(A_11,A_12)
        S_3=Matrix_Add(A_21,A_22)
        S_4=Matrix_Sub(B_21,B_11)
        S_5=Matrix_Add(A_11,A_22)
        S_6=Matrix_Add(B_11,B_22)
        S_7=Matrix_Sub(A_12,A_22)
        S_8=Matrix_Add(B_21,B_22)
        S_9=Matrix_Sub(A_11,A_21)
        S_10=Matrix_Add(B_11,B_12)
        #Step 3 Create 7 matrix P_1...P_7 by Multiply
        P_1=Matrix_Multiply(A_11,S_1)
        P_2=Matrix_Multiply(S_2,B_22)
        P_3=Matrix_Multiply(S_3,B_11)
        P_4=Matrix_Multiply(A_22,S_4)
        P_5=Matrix_Multiply(S_5,S_6)
        P_6=Matrix_Multiply(S_7,S_8)
        P_7=Matrix_Multiply(S_9,S_10)
        #Step 4 Caculate C_11...C22
        C_11=Matrix_Sub(Matrix_Add(Matrix_Add(P_5,P_4),P_6),P_2)
        C_12=Matrix_Add(P_1,P_2)
        C_21=Matrix_Add(P_3,P_4)
        C_22=Matrix_Sub(Matrix_Add(P_5,P_1),Matrix_Add(P_3,P_7))
        C=Combine(C_11,C_12,C_21,C_22)
    return(C)

#test
test=Matrix_Multiply(A,B)
print(A)
print(B)
print(test)
        
        
        
 
