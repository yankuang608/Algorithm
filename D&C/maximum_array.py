#maximum subarray
def Find_Maximum_Crossing_Subarray(A,low,mid,high):
    sum=0
    left_sum=-10000000#represent negtive infinite
    for i in range(mid,low-1,-1):
        sum+=A[i]
        if sum>left_sum:
            left_sum=sum
            max_left=i
    sum=0
    right_sum=-10000000
    for j in range(mid+1,high+1):
        sum+=A[j]
        if sum>right_sum:
            right_sum=sum
            max_right=j
    return(max_left,max_right,left_sum+right_sum)

def Find_Maximum_Subarray(A,low,high):
    if low==high:
        return(low,high,A[low])
    else:
        mid=(low+high)//2
        (left_low,left_high,left_sum)=Find_Maximum_Subarray(A,low,mid)
        (right_low,right_high,right_sum)=Find_Maximum_Subarray(A,mid+1,high)
        (cross_low,cross_high,cross_sum)=Find_Maximum_Crossing_Subarray(A,low,mid,high)
        if left_sum>right_sum and left_sum>cross_sum:
            return(left_low,left_high,left_sum)
        elif right_sum>left_sum and right_sum>cross_sum:
            return(right_low,right_high,right_sum)
        else:
            return(cross_low,cross_high,cross_sum)
    
#test
array=(213,6,8,-23,-12,-22,-12,-5,-8,36)
result=Find_Maximum_Subarray(array,0,len(array)-1)
print("low=",result[0],"high=",result[1],"sum=",result[2])

            
