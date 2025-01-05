class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        # First: Calculate total shifts
        n = len(s)
        shift_accum = [0] * (n + 1)
        
        for start, end, direction in shifts:
            shift_accum[start] += 1 if direction == 1 else -1
            shift_accum[end + 1] -= 1 if direction == 1 else -1
        
        current_shift = 0
        result = []
        min_value = ord('a')
        domain_size = ord('z') - min_value + 1
        
        for i in range(n):
            current_shift += shift_accum[i]
            new_char = chr((ord(s[i]) - min_value + current_shift) % domain_size + min_value)
            result.append(new_char)

        return ''.join(result)
