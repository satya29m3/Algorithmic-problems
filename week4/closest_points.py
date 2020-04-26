def find_min(new_points,d):
    d_min = d
    for i in range(len(new_points)):
        j = i+1
        num = j+7
        while(j<num and j<len(new_points)):
            dist = (((new_points[i][0] - new_points[j][0])**2)+ ((new_points[i][1] - new_points[j][1])**2))**(1/2)
            d_min = min(d_min,dist)

            j+=1

    return d_min

def closest_point(points,low,high):
    if(high-low==1):
        d = ((points[low][0] - points[high][0])**2) + ((points[low][1] - points[high][1])**2)
        return d**(1/2)        

    if(high==low):
        d = ((points[low][0])**2) + ((points[low][1])**2)
        return d**(1/2)
    
    mid = int(low + (high-low)/2)
    d1 = closest_point(points,low,mid)
    d2 = closest_point(points,mid+1,high)
    d = min(d1,d2)
    new_points = []
    mid_line = points[mid][0]
    for i in range(low,mid+1):
        dist = ((points[i][0]-mid_line)**2)**(1/2)
        if(dist<=d):
            new_points.append(points[i])

    for i in range(mid+1,high+1):
        dist = ((points[i][0]-mid_line)**2)**(1/2)
        if(dist<=d):
            new_points.append(points[i])
    
    new_points.sort(key = lambda y:y[1])
            

    d_min = find_min(new_points,d)
    return d_min


if __name__=="__main__":
    n = int(input())
    points = []
    for i in range(n):
        (a,b) = [int(x) for x in input().split()]
        points.append((a,b))
    points.sort(key=lambda x:x[0])
    print("{0:.6f}".format(closest_point(points,0,n-1)))


