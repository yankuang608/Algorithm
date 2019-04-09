array = [2,5,8,9]
maxsize=10
top=len(array)
def push(element):
    global top
    global array
    if top>maxsize:
        print('stack overflow')
    else:
        array[top]=element
        top+=1
def pop(element):
    global top
    global array
    for pop_number in range(0,element):
        if top==0:
            print('stack is empty')
        else:
            top-=1
            print(array[top-1])

push(3)
push(4)
pop(2)