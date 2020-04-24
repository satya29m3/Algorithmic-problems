def max_prizes(total):
    if(total<=2):
        print(1)
        print(total)
        return
    tot = total    
    sum_val = 0
    i = 1
    length = 0
    current = 0
    while((total-i)>0):
        sum_val+= i
        total -=i
        current = i
        length+=1
        i+=1

    if(total>current):
        current =total
        length+=1
    else:
        current = current + total
    print(length)


    for i in range(1,length):
        print(i,end=' ')
    print(current)
    

if __name__=="__main__":
    total = int(input())
    max_prizes(total)