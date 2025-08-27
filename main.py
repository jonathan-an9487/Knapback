import pandas as pd 
def Snapback(item_value, item_weight, bpCapacity):
    item = len(item_value)
    dp = [[0 for _ in range(bpCapacity + 1)] for _ in range(item + 1)]

    for i in range(1, item+1):
        for w in range(0, bpCapacity + 1):
            if item_weight[i - 1] <= w:
                dp[i][w] = max(
                    item_value[i - 1] + dp[i - 1][w - item_weight[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]
    print(pd.DataFrame(dp))
    return dp[item][bpCapacity]


if __name__ == "__main__":
    item_value = [60, 100, 120]
    item_weight = [10, 20, 30]
    bpCapacity = 50
    print("能裝最大價值為:",Snapback(item_value, item_weight, bpCapacity))
