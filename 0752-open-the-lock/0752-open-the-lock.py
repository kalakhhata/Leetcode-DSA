class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        visited=set(deadends)
        if '0000' in visited:
            return -1
        
        q=deque()
        q.append((0,'0000'))
        visited.add('0000')

        while q:
            turn,code=q.popleft()
            if code==target:
                return turn

            for i in range(4):
                digit=int(code[i])

                new_digit=(digit+1)%10
                new_code=code[:i]+str(new_digit)+code[i+1:]

                if new_code not in visited:
                    visited.add(new_code)
                    q.append((turn+1,new_code))
                
                new_digit=(digit-1)%10
                new_code=code[:i]+str(new_digit)+code[i+1:]

                if new_code not in visited:
                    visited.add(new_code)
                    q.append((turn+1,new_code))
        return -1

