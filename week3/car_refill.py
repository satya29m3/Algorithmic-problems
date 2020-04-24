def car_refill(d,m,n,stops):
    stops.append(d)
    stops.insert(0,0)
    numrefill = 0
    currentrefill = 0
    while(currentrefill<=n):
        lastrefill = currentrefill
        while(currentrefill<=n and (stops[currentrefill+1]-stops[lastrefill])<=m):
            currentrefill += 1
        if(currentrefill==lastrefill):
            return -1
        if(currentrefill<=n):
            numrefill+=1
    return numrefill
    

if __name__=="__main__":
    d = int(input())
    m = int(input())
    n = int(input())
    stops = [int(x) for x in input().split()]
    print(car_refill(d,m,n,stops))