#maximum subarray linear-time
def Find_Maximum_Subarray(A):
    n=len(A)
    sum=0
    max=-10000000
    for i in range(0,n):
        sum+=A[i]
        if sum>max:
            max=sum
            high=i
    sum=0
    max=-10000000
    for j in range(n-1,-1,-1):
        sum+=A[j]
        if sum>max:
            max=sum
            low=j
    sum=0
    for m in range(low,high+1):
        sum+=A[m]
    return(low,high,sum)

#test
array=(213,6,8,-23,-12,-22,-12,-5,-8,36)
result=Find_Maximum_Subarray(array)
print("low=",result[0],"high=",result[1],"sum=",result[2])
