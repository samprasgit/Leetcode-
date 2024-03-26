# 1  [0121. 买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/)


## 题目大意
**描述**：给定一个数组 `prices` ，它的第 `i` 个元素 `prices[i]` 表示一支给定股票第 `i` 天的价格。只能选择某一天买入这只股票，并选择在未来的某一个不同的日子卖出该股票。

**要求**：计算出能获取的最大利润。如果你不能获取任何利润，返回 0。

**说明**：

- $1 \leq prices.length \leq 10^5$
- $0 \leq  prices[i] \leq 10^4$

**示例**：

- 示例 1：

```
输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
```

- 示例 2：

```
输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
```
  
## 解题思路

### 思路 1：

暴力法
### 思路 1：代码

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0 
        for  i in range( len(prices)): 
            for j in range(i+1,len(prices)) : 
                res = max(res, prices[j] - prices[i]) 
        return res 
  

```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2)$
- **空间复杂度**：$O(1)$

### 思路 2：

贪心算法：得到左边最小值，右边最大的值，得到的差值就是最大利润
### 思路 2：代码


```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = max(prices )
        res =0 
        for i in range(len(prices)) : 
            low = min(low,prices[i]) 
            res = max(res,prices[i]-low)

        return res 
  

```

### 思路 2：复杂度分析

- **时间复杂度**：$O(n)$
- **空间复杂度**：$O(1)$
- 
### 思路 3：
动态规划

### 思路：代码

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if len == 0:
            return 0
        dp = [[0] * 2 for _ in range(length)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, length):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], prices[i] + dp[i-1][0])
        return dp[-1][1]
```

### 思路 3：复杂度分析

- **时间复杂度**：$O(n)$
- **空间复杂度**：$O(1)$

# 2  [0122. 买卖股票的最佳时机]([. - 力扣（LeetCode）](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/))


## 题目大意
**描述**：给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

**要求**：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

**说明**：

- $1 \leq prices.length \leq3*10^4$
- $0 \leq  prices[i] \leq 10^4$

**示例**：

- 示例 1：

```
输入：prices = [7,1,5,3,6,4]
输出：7
解释：在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6 - 3 = 3 。
     总利润为 4 + 3 = 7。V
```

- 示例 2：

```
输入：prices = [1,2,3,4,5]
输出：4
解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4 。
     总利润为 4 。
```
  
## 解题思路

### 思路 1：

动态规划
### 思路 1：代码

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        dp = [[0] * 2 for _ in range(length)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, length):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i]) #注意这里是和121. 买卖股票的最佳时机唯一不同的地方
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        return dp[-1][1]
  

```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$
- **空间复杂度**：$O(1)$

