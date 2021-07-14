from typing import List

# template 1
# * search for an element or condition which can be
# determined by accessing one single element of the array
# syntax
# * initial condition: left, right = 0, length-1
# * termination: left > right (e.g. while left <= right)
# * searching left: right = mid - 1
# * searching right: left = mid + 1


class BinarySearch:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


class Sqrt:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return right


class Guesser:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            r = guess(mid)
            if r == 0:
                return mid
            elif r == 1:
                left = mid + 1
            else:
                right = mid - 1


class RotatedSortedArray:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[left] > nums[mid]:
                right = mid
            elif nums[left] < nums[mid]:
                left = mid
            else:
                break
        # print(left)
        # print(right)
        if (target >= nums[0]) & (target <= nums[left]):
            l, r = 0, left
        elif (target >= nums[right]) & (target <= nums[len(nums) - 1]):
            l, r = right, len(nums) - 1
        else:
            return -1
        # print(l)
        # print(r)

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return -1


# Template 2
# It is an advanced form of the binary search
# Used to search an element or condition that requires
# accessing the current index and its immediate right neighbor
# gurantees the search space is at least two at each step
# post processing is required, loop or recursion ends when one
# element is left, need to check if this element satisfies the
# condition

# syntax
# Initialization: left = 0, right = length
# termination: left=right
# searching left: right = mid
# searching right: left = mid + 1


class FirstBadVersion:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1
        left, right = 1, n

        while left < right:
            mid = left + (right - left) // 2
            # print(mid)

            gmid = isBadVersion(mid)
            gmid_next = isBadVersion(mid + 1)
            # print(gmid)
            # print(gmid_next)

            if gmid == False:
                if gmid_next == True:
                    return mid + 1
                else:
                    left = mid + 1
            else:
                right = mid


class PeakFinder:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        n = len(nums)

        if nums[0] > nums[1]:
            return 0
        if nums[n - 1] > nums[n - 2]:
            return n - 1
        left, right = 0, n - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left


class MinFinder:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[0] < nums[n - 1]:
            return nums[0]  # non rotated
        if nums[n - 1] < nums[n - 2]:
            return nums[n - 1]

        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            # print(f'{left}{right}{mid}')
            if left == mid:
                break
            if nums[mid] > nums[left]:
                left = mid
            else:
                right = mid

        return nums[left + 1]


## Template 3
# Used to search for an element or condition which requires
# accessing the current index + its immediate left and right neighbors
# Use element's neighbors to determine if condition is met
# and decide whether to go left or right
# Gurantees Search Space is at least 3 in size at each step
# Post-processing required.
# Loop/Recursion ends when you have 2 elements left.
# Need to assess if the remaining elements meet the condition.


class ClosestKElements:
    def search(self, arr: List[int], k: int, x: int) -> List[int]:

        left, right = 0, len(arr) - k

        while left < right:
            mid = left + (right - left) // 2

            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left : left + k]

