#! /usr/bin/python3
#
# Title:dedupe1.py
# Description: move duplicate elements to end of array
# Development Environment:OS X 10.10.5/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#
class Solution:
    def removeDuplicates1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print(nums)

        match = 0
        ndx2 = len(nums) -1
        for ndx1 in range(len(nums)-2, -1, -1):
            print("%d:%d" % (ndx1, ndx2))
            if nums[ndx1] == nums[ndx2]:
                print("duplicate %d:%d:%d" % (ndx1, nums[ndx1], nums[ndx2]))

                match = match+1
                temp = nums[ndx2];
                for ndx3 in range(ndx2, len(nums)-1):
                    print("ndx3:%d" % ndx3)
                    nums[ndx3] = nums[ndx3+1]

                nums[len(nums)-1] = temp
            else:
                print("not duplicate %d:%d:%d" % (ndx1, nums[ndx1], nums[ndx2]))

            ndx2 = ndx2-1

        print(nums)

        return len(nums)-match

    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print(nums)

        if len(nums) < 2:
            return len(nums)

        jj = 0
        for kk in nums[1:]:
            if kk != nums[jj]:
                jj += 1
                nums[jj] = kk

        print(nums)

        return jj+1

print('start');

#
# argv[1] = configuration filename
#
if __name__ == '__main__':
    print('main')

    solution = Solution()
    xx = solution.removeDuplicates2([1, 1, 2])
    print(xx)

print('stop')
