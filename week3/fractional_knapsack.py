def fractional_knapsack(capacity,weights,values):
    items = [0]*capacity
    value = 0
    for k in range(len(weights)):
        if capacity==0:
            return value
        index = 0
        for i in range(len(weights)):
            if(weights[i]>0 and (values[i]/weights[i])>(values[index]/weights[index])):
                index = i
        a = min(weights[index],capacity)
        value += a*(values[index]/weights[index])
        weights[index] -= a
        items[index] += a
        capacity -= a 
    return value


if __name__=="__main__":
    [n,capacity] = [int(x) for x in input().split()]
    weights = []
    values = []
    for i in range(n):
        [v,w] = [int(x) for x in input().split()]
        weights.append(w)
        values.append(v)
    print(fractional_knapsack(capacity,weights,values))
