def collect_sign(n, timings):
    num = 0
    points = []
    timings.sort(key=lambda x: x[1])
    i =0
    while(i<n):
        t = timings[i][1]
        count = 1
        truth_val = 0 
        for j in range(i+1,n):
            if(t<timings[j][0]):
                points.append(t)
                i = j-1
                truth_val = 1
                break
            count+=1


        if(count==(n-i) and truth_val==0):
            points.append(t)
            break
        i+=1


    print(len(points))
    print(' '.join([str(x) for x in points]))
    return 

if __name__=="__main__":
    n = int(input())
    timings = []
    for i in range(n):
        time = [int(x) for x in input().split()]
        timings.append(time)
    collect_sign(n,timings)