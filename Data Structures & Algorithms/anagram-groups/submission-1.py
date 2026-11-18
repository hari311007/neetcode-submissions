class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord("a")]+=1
            result[tuple(count)].append(s) #we cant add a list as a key in python so we r converting i tto tuple since it is immutable
        return list(result.values())
#working:
# each string characters will be counted and is stored in hash map as a key and then if another string has the same key it gets appened or else the key is created that why we r using defaultdict(list) when we using result[tuple(count)] sometimes the key may not exist and it will throw a keyerror to avoid it we r using the defaultdict(list)(it belongs to collection module). it creates a empty list for the non existent keys and then append and also list cant be keys as they r mutable so typecasting them to tuple
#time complexity:
# Time complexity: O(n⋅k)
# Space complexity: O(n⋅k)

# n is the number of strings in strs
# k is the maximum length of a string in strs
