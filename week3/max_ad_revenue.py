def sorting(n,x):
    for k in reversed(range(n)):
        index = 0
        for i in range(k+1):
            if(x[i]>x[index]):
                index = i
        temp = x[k]
        x[k] = x[index]
        x[index] = temp
        del temp
    return x

def max_ad_rev(n,a,b):
    a = sorting(n,a)
    b = sorting(n,b)
    summ = 0
    for i in range(n):
        summ += a[i]*b[i]
    return summ

if __name__=="__main__":
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    print(max_ad_rev(n,a,b))
