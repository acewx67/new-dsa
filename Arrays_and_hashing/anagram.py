def isAnagram(s: str, t: str) -> bool:
        # Optimized
        # hm1 = {}
        # hm2 = {}
        # def create_hm(string,hm):
        #     for char in string:
        #         if char in hm:
        #             hm[char] += 1
        #         else:
        #             hm[char] = 1
        #     return hm
        # if create_hm(s,hm1) == create_hm(t,hm2):
        #     return True
        # return False

        # Brute
    print(sorted(s) == sorted(t))

isAnagram("anagram", "nagarm")