import random
def partition(A,l,r):
    x = A[l]
    j = l
    for i in range(l+1,r+1):
        if(A[i]<=x):
            j +=1
            # SWAP {A[i] and A[j]}
            temp = A[j]
            A[j] = A[i]
            A[i] = temp
    temp = A[j]
    A[j] = A[l]
    A[l] = temp
    return j        

def random_partition(A,l,r):
    x = A[l]
    j = l
    for i in range(l+1,r+1):
        if(A[i]<x):
            j +=1
            # SWAP {A[i] and A[j]}
            temp = A[j]
            A[j] = A[i]
            A[i] = temp
    temp = A[j]
    A[j] = A[l]
    A[l] = temp
    m1 = j
    for i in range(m1+1,r+1):
        if(A[i]==x):
            j +=1
            # SWAP {A[i] and A[j]}
            temp = A[j]
            A[j] = A[i]
            A[i] = temp
    temp = A[j]
    A[j] = A[m1]
    A[m1] = temp
    m2 = j
    return m1,m2



def quicksort(A,l,r):
    if(l>=r):
        return 

    m = partition(A,l,r)
    quicksort(A,l,m-1)
    quicksort(A,m+1,r)

def random_quicksort(A,l,r):
    if(l>=r):
        return
    k = random.randint(l,r)
    temp = A[k]
    A[k] = A[l]
    A[l] = temp
    del temp

    m1,m2 = random_partition(A,l,r)
    random_quicksort(A,l,m1-1)
    random_quicksort(A,m2+1,r)

if __name__=="__main__":
    n = int(input())
    A = [int(x) for x in input().split()]
    random_quicksort(A,0,n-1)
    print(' '.join([str(x) for x in A]))