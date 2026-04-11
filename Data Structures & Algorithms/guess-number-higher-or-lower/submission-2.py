# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        l, r = 1, n

        while l <= r:
            pick = (l + r) // 2

            guess1 = guess(pick)

            if guess1 == -1:
                r = pick - 1

            elif guess1 == 1:
                l = pick + 1

            else:
                return pick
            
                