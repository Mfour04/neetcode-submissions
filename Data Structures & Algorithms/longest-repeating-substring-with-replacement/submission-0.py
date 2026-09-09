class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_frequency = 0
        max_length = 0
        l = 0 

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_frequency = max(max_frequency, count[s[r]])
            window_length = r - l + 1
            replace = window_length - max_frequency

            if replace > k:
                count[s[l]] -= 1
                l += 1

            max_length = max(max_length, r - l + 1)
        return max_length 

