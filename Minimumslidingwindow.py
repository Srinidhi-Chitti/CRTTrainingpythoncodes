from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = Counter(t)
        have = {}
        required = len(need)
        formed = 0

        l, r = 0, 0
        min_len = float('inf')
        min_window = (0, 0)

        while r < len(s):
            char = s[r]
            have[char] = have.get(char, 0) + 1

            if char in need and have[char] == need[char]:
                formed += 1

            while l <= r and formed == required:
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    min_window = (l, r)

                have[s[l]] -= 1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    formed -= 1
                l += 1

            r += 1

        if min_len == float('inf'):
            return ""
        return s[min_window[0]:min_window[1] + 1]
