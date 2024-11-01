with open("LAB4/example2.txt", "r") as file:
    # Read the entire file content
    money = int(file.readline().strip("\n"))
    coins = [int(c) for c in file.readline().strip("\n").split(",")]

def changeProblem(coins, amount):
    # initialize array with size amount + 1 and set all values to inf
    array = [float('inf')] * (amount + 1)
    # store minimum # of coins for each amount from 0 to 'amount'
    # setting to infinity represents that initially, it's impossible to make that amount
    array[0] = 0  # Base case: 0 coins needed to make amount 0

    # iterate through all values from 1 to amount
    for i in range(1, amount + 1):
        # interate through every coin in coins
        for coin in coins:
            # if the coin can go into i, consider using that coin:
            if coin <= i:  # If the coin can contribute to the amount
                array[i] = min(array[i], 1 + array[i - coin])
                # 1 + array[i - coin]
                    # 1 is using that coin
                    # array[i-coin] is a previously calculated min
        print("amount: ", i,"| # of coins: ", array[i])
    # if array[amount] != inf then change can be made
    if array[amount] != float('inf'):
        return array[amount]
    else:
        return -1

result = changeProblem(coins, money)
if result != -1:
    print(f"The minimum number of coins needed to make {money} is: {result}")
else:
    print(f"It's not possible to make the amount {money} with the given coins.")