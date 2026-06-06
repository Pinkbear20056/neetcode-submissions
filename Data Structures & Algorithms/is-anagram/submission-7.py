class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        list_s = []
        list_t = []

        for i in range(len(s)):
            list_s.append(s[i])
            list_t.append(t[i])

        # 리스트에 넣어서 정렬하기
        sorted_list_s = sorted(list_s)
        sorted_list_t = sorted(list_t)

        for i in range(len(sorted_list_s)):
            if sorted_list_s[i] == sorted_list_t[i]:
                continue
            else:
                return False
        
        return True

        

        