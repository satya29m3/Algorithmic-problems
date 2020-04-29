def primitive_calc(n):
    if n==1:
        return 1
    num3 = 0
    num2 = 0
    num1 = 0
    if n%3==0:
        num3 = primitive_calc(n/3)
    if n%2 ==0:
        num2 = primitive_calc(n/2)
    num1 = primitive_calc(n-1)
    return num1 +num2+ num3

def rec_way(n,operations):
    if n==1:
        return 0

    minop = float('inf') 
    for i in operations:
        op_val = float('inf')
        if(i==1):
            op_val = n-1
        if(i==2):
            if(n%2==0):
                op_val = n/2
        if(i==3):
            if(n%3==0):
                op_val = n/3
        if(op_val<=n):
            numop = rec_way(op_val,operations)
            if(numop+1<minop):
                minop = numop+1
    return minop

def DP_way(n,operations):
    minop1 = [0]*(2)
    minop2 = [float('inf')]*(n-1)
    minop = minop1+minop2
    for val in range(2,n+1):

        for i in operations:
            op_val = val
            if(i==1):
                op_val = int(val-1)
            if(i==2 and val%2 == 0):
                op_val = int(val/2)
            if(i==3 and val%3 == 0):
                op_val = int(val/3)
            if(op_val<val):
                numop = minop[op_val] + 1
                if(numop<minop[val]):
                    minop[val] = numop

    return minop[n]



if __name__=="__main__":
    n = int(input())
    operations = [1,2,3]
    print(DP_way(n,operations))