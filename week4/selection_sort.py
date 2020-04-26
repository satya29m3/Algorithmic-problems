def selection_sort(elem,n):
    for i in range(n):
        minindex = i
        for j in range(i+1,n):
            if(elem[j]<elem[minindex]):
                minindex=j
        temp = elem[i]
        elem[i] = elem[minindex]
        elem[minindex] = temp

    return elem

if __name__=="__main__":
    n = int(input())
    elem = [int(x) for x  in input().split()]
    val = selection_sort(elem,n)
    for i in range(n):
        print(val[i],end=' ')
    print()