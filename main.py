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


# import pandas as pd
#  函數 0/1背包問題(物品價值陣列, 物品重量陣列, 背包容量)
#     取得 物品數量長度 len n
#     建立 二維陣列 dp，大小為 (n+1)這在後 x (容量+1)這在前，初始值為 0

#     對 每個物品 i 從 1 到 n+1 做：
#         對 每個當前容量 w 從 0 到 背包容量+1 做：
#             如果 當前物品重量 <= 當前容量：
#                 dp[i][w] = 最大值(
#                     放入當前物品的價值 + dp[前i-1物品][剩餘容量(w-item_weight)],
#                     不放入當前物品的 dp[前i-1物品][當前容量]
#                 )
#             否則：
#                 dp[i][w] = dp[前i-1物品][當前容量]

#     print(pd.DataFrame(dp))這樣顯示比較好看
#     返回 dp[n][背包容量]  # 最終最大價值

# 主程式
# 物品價值 = [60, 100, 120]
# 物品重量 = [10, 20, 30]
# 背包容量 = 50
# 呼叫 0/1背包問題(物品價值, 物品重量, 背包容量)


