#! /usr/bin/python3
#
# Title:buy_sell1.py
# Description: find max profit
# Development Environment:OS X 10.10.5/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        print(prices)

        profit = 0
        bought = -1

        for ndx in range(len(prices)-1):
            print("ndx:%d:%d" % (ndx, prices[ndx]))
            if prices[ndx] > prices[ndx+1]:
                print("sell:%d" % prices[ndx])
                if bought >= 0:
                    profit += prices[ndx] - bought
                    bought = -1
            else:
                print("buy:%d" % prices[ndx])
                if bought < 0:
                    bought = prices[ndx]

        if bought > -1:
            profit += prices[len(prices)-1] - bought

        return profit

print('start');

#
# argv[1] = configuration filename
#
if __name__ == '__main__':
    print('main')

    solution = Solution()
    print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
    print(solution.maxProfit([1, 2, 3, 4, 5]))
    print(solution.maxProfit([7, 6, 4, 3, 1]))
    print(solution.maxProfit([2, 1, 2, 0, 1]))

print('stop')
