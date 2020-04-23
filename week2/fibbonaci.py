def fibbonacci(n):
    if n<=1:
        return 1
    return fibbonacci(n-1)+fibbonacci(n-2)

def fibbonacciFAST(n):
    a = [0,1]
    if n<=1:
        return n
    
    for i in range(2,n+1):
        x = a[0]
        y = a[1]
        a[0] = y
        a[1] = x+y
    return a[1]

if __name__=="__main__":
    n = int(input())
    print(fibbonacciFAST(n))
