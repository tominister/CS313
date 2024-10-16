"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Haoran Fang and Kevin Yu, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: hf5829
UT EID 2: kjy355
"""


def group_sum(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to the
    given target.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start>=len(nums):
        return target==0
    if group_sum(start+1,nums,target-nums[start]):
        return True
    return group_sum(start+1,nums,target)


def group_sum_6(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to the
    given target. Additionally, if there is are 6's present in the array, they must all
    be chosen.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start>=len(nums):
        return target==0
    if nums[start]==6:
        return group_sum_6(start+1,nums,target-nums[start])
    if group_sum_6(start+1,nums,target-nums[start]):
        return True
    return group_sum_6(start+1,nums,target)


def group_no_adj(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if a value is chosen, the value immediately after
    (the value adjacent) cannot be chosen.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start>=len(nums):
        return target==0
    if group_no_adj(start+2,nums,target-nums[start]):
        return True
    return group_no_adj(start+1,nums,target)


def group_sum_5(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if a multiple of 5 is in the array, it must be included
    If the value immediately following a multiple of 5 if 1, it must not be chosen

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start>=len(nums):
        return target==0
    if nums[start]==5:
        if start+1<len(nums) and nums[start+1]==1:
            return group_sum_5(start+2,nums,target-nums[start])
        return group_sum_5(start+1,nums,target-nums[start])
    if group_sum_5(start+1,nums,target-nums[start]):
        return True
    return group_sum_5(start+1,nums,target)


def group_sum_clump(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if there is a group of identical numbers in succession,
    they must all be chosen, or none of them must be chosen.
    EX: [1, 2, 2, 2, 5, 2], all three of the middle 2's must be chosen, or none of them must be
    chosen to be included in the sum. One loop is allowed to check for identical numbers.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    def helper(start, nums, target):
        if start >= len(nums):
            if target == 0:
                return True
            else:
                return False
        sum1 = nums[start]
        start1 = start + 1
        while start1 < len(nums) and nums[start1] == nums[start]:
            sum1 += nums[start1]
            start1 += 1

        if helper(start1, nums, target - sum1):
            return True

        if helper(start1, nums, target):
            return True
        return False
    return helper(start, nums, target)


def split_array(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of these two groups must be equal
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    total=sum(nums)/2
    def helper(nums, n, CurrSum, total):
        if CurrSum==total:
            return True
        elif CurrSum>total:
            return False
        if n == len(nums):
            return CurrSum == total
        if helper(nums, n+1, CurrSum+nums[n], total):
            return True
        if helper(nums, n+1, CurrSum, total):
            return True
        return False
    return helper(nums, 0, 0, total)


def split_odd_10(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of one group must be odd, while the other group must be a multiple of 10
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    def helper(nums, n, odd, ten):
        if n==len(nums):
            return odd%2==1 and ten%10==0
        if helper(nums, n+1,odd+nums[n], ten):
            return True
        if helper(nums, n+1,odd, ten+nums[n]):
            return True
        return False
    return helper(nums, 0, 0, 0)


def split_53(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of these two groups must be equal
    Additionally, all multiples of 5 must be in one group, and all multiples of 3 (and not 5)
    must be in the other group
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    if len(nums)==0:
        return False
    def helper(nums, n, group1, group2):
        if n==len(nums):
            return group1==group2

        if nums[n]%5==0:
            if helper(nums, n+1, group1+nums[n], group2):
                return True
        elif nums[n]%3==0:
            if helper(nums, n+1, group1, group2+nums[n]):
                return True
        else:
            if helper(nums, n+1, group1+nums[n], group2):
                return True
            if helper(nums, n+1, group1, group2+nums[n]):
                return True
        return False
    return helper(nums, 0, 0, 0)
