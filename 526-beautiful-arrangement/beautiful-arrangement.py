class Solution:
    def countArrangement(self, n: int) -> int:
        used = [False] * (n + 1)

        def backtrack(position):
            if position > n:
                return 1

            ret = 0

            for num in range(1, n + 1):
                if not used[num]:
                    if num % position == 0 or position % num == 0:
                        used[num] = True

                        ret += backtrack(position + 1)

                        used[num] = False

            return ret

        return backtrack(1)