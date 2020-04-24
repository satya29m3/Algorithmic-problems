def money_change(total):
    coin_type = [10,5,1]
    coins = 0
    for coin in coin_type:
        i_coins = int(total/coin)
        total = total%coin
        coins+=i_coins
    return coins


if __name__=="__main__":
    total_money = int(input())
    print(money_change(total_money))