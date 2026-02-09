class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = low + (high - low) // 2
            missing_idx = arr[mid] - (mid + 1)  # number of missing numbers up to index mid

            if missing_idx < k:
                low = mid + 1
            else:
                high = mid - 1   # <-- here you had `right`, should be `high`
        
        return low + k
