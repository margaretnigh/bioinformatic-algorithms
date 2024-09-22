with open("rosalind_ba5a.txt", "r") as file:
    # Read the entire file content
    money = int(file.readline().strip("\n"))
    coins = [int(c) for c in file.readline().strip("\n").split(",")]

def changeProblem(coins[], amount):
    # initialize array with size amount + 1 and set all values to inf
    # store minimum # of coins for each amount from 0 to 'amount'
    # setting to infinity represents that initially, it's impossible to make that amount
    array[0] = 0
    # base case
    # no coins needed to make 0

    # iterate through all values from 1 to amount
        # interate through every coin in coins
            # if the coin can go into i, consider using that coin:
                min(array[i], 1 + array[i - coin])
                # array[i] = inf for initial amounts
                # 1 + array[i - coin]
                    # 1 is using that coin
                    # array[i-coin] is a previously calculated min
    # if array[amount] != inf then change can be made
    return array[amount]