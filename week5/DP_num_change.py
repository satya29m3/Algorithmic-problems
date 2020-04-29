def DPchange(money,coins):
    mincoins = [0]*(money+1)
    
    for m in range(1,money+1):
        mincoins[m] = float('inf')
        for i in range(len(coins)):
            if m>=coins[i]:
                numcoin = mincoins[m-coins[i]] + 1
                if numcoin<mincoins[m]:
                    mincoins[m] = numcoin
    return mincoins[money]


if __name__=="__main__":
    denominatoins = [1,3,4]
    money = int(input())
    print(DPchange(money,denominatoins))
