def Selection_Sort(A):
    for j in range(0,len(A)-1):
        key=j
        for i in range(j+1,len(array)):#find the smallest number array[key] in array[j+1...]
            if array[i]<array[key]:
                key=i
            exchange=array[key]
            array[key]=array[j]
            array[j]=exchange
    return(A)
