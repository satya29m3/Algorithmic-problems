from collections import Counter
def merge(left,right):
    val = dict()
    keys = set(list(left.keys()) + list(right.keys()))
    for i in keys:
        if (i in left.keys() and i in right.keys()):
            val[i] = left[i] + right[i]
        elif(i in left.keys()):
            val[i] = left[i]
        elif(i in right.keys()):
            val[i] = right[i]

    return val



def organize(start,end,low,high,points):
    if(high == low):
        val = dict()
        for i in points:
            if(start[low]<=i<=end[low]):
                val[i] =1
        return val

    mid = int(low + (high-low)/2)

    left = organize(start,end,low,mid,points)
    right = organize(start,end,mid+1,high,points)
    ret_val = merge(left,right)

    
    return ret_val

def faster_way(n,m,start,end,points):
    main_list = []
    for i in range(n):
        main_list.append((start[i],'l'))
        main_list.append((end[i],'r'))
    for i in range(m):
        main_list.append((points[i],'p'))
    main_list.sort()
    return main_list



def freq_arange(points,sorted_points):
    freq = dict()
    for i in sorted_points:
        if i in freq.keys():
            freq[i] +=1
        else:
            freq[i] = 1
    ans = []
    for p in points:
        if p in freq.keys():
            ans.append(freq[p])
        else:
            ans.append(0)
    return ans



if __name__=="__main__":
    [n,m] = [int(x) for x in input().split()]
    start = []
    end = []
    for i in range(n):
        [s,e] = [int(x) for x in input().split()]
        start.append(s)
        end.append(e)
    points = [int(x) for x in input().split()]

    main_list = faster_way(n,m,start,end,points)
    
    point_dict = dict()
    cnt = 0
    for i in main_list:
        if (i[1]=='l'):
            cnt+=1
        elif (i[1]=='r'):
            cnt-=1
        else : point_dict[i[0]] = cnt



    # ans = organize(start,end,0,n-1,points)

    for i in points:
        if(i in point_dict.keys()):
            print(point_dict[i] ,end=' ')
        else:print(0,end = ' ')
    print()

