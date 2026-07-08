class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        rem_count = {}

        # Count the frequency of each remainder
        for num in arr:
            rem = num % k
            rem_count[rem] = rem_count.get(rem, 0) + 1

        # Check each remainder
        for rem, cnt in rem_count.items():

            # Remainder 0 must have an even count
            if rem == 0:
                if cnt % 2 != 0:
                    return False

           

            # Other remainders must match their complement
            elif cnt != rem_count.get(k - rem, 0):
                return False

        return True