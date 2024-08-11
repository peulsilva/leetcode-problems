class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = {}
        for c in word:
            if c not in counter:
                counter[c] = 0
            
            counter[c] += 1
        
        list_counter = [v for v in counter.values()]
        list_counter= sorted(list_counter, reverse = True)

        ans = 0
        i = 0
        for idx, n_appearances in enumerate(list_counter):
            if idx% 8 ==0:
                i += 1

            ans += n_appearances * i

        return ans
