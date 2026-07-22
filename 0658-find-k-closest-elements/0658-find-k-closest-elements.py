class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        abs_list = list(map(lambda n: abs(n - x), arr))
        abs_sum_min = abs_sum = sum(abs_list[0:k])
        min_i = 0

        for i in range(1, len(arr) - k + 1):
            abs_sum = abs_list[i + k - 1] + abs_sum - abs_list[i - 1]

            if abs_sum < abs_sum_min:
                abs_sum_min = abs_sum
                min_i = i

        return arr[min_i:min_i + k]