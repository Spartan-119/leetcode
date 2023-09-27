class Solution:
	def maxProfit(self, prices) -> int:
		left = 0
		right = 1
		profit = 0

		while right < len(prices):
			current_profit = prices[right] - prices[left]
			if prices[left] < prices[right]:
				profit = max(current_profit, profit)
			else:
				left = right
			right += 1

		return profit


# creating the main function
if __name__ == '__main__':
	solution = Solution()
	test_cases = [
	[7,1,5,3,6,4],
	[7,6,4,3,1]
	]

	for i in test_cases:
		print(solution.maxProfit(i))
