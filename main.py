'''
arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
return_dict = {}

for i in range(len(arr)):
    if arr[i] not in return_dict:
        return_dict[arr[i]] = 1
    else:
        continue

#print(list(return_dict))


###########################
arr2 = [2, 2, 2, 2, 2]
hash_set = set()

for i in range(len(arr2)):
    if arr2[i] not in hash_set:
        hash_set.add(arr2[i])
#print(list(hash_set))


#########################

# Two pointers
arr3 = [1, 2, 2, 3, 4, 4, 4, 5, 5]

write = 1

for read in range(1,len(arr3)):
    if arr3[read] != arr3[read-1]:
        #print(f"arr read {arr3[read]} and arr write {arr3[write]}")
        arr3[write] = arr3[read]
        #print(f"arr {arr3}")
        write += 1


#print(arr3[:write])



nums = [-4,-1,0,-3,10]

left = 0
right = len(nums) - 1
result_arr5 = []

while left <= right:
    if abs(nums[left]) > abs(nums[right]):
        result_arr5.append(nums[left] ** 2)
        left += 1
    else:
        result_arr5.append(nums[right] ** 2)
        right -= 1
result_arr5.reverse()
#print(result_arr5)

'''

'''
Generating All Subarrays

Given an array arr[], the task is to generate all the possible subarrays of the given array.
arr = [1, 2,3,4]
return_arr = []


for i in range(len(arr)):
        for j in range(i+1,len(arr)+1):
                if arr[i:j] == []:
                        continue
                return_arr.append(arr[i:j])

print(return_arr)
'''

'''
Reverse an array arr[]. Reversing an array means 
rearranging the elements such that the first element becomes the last, the second element becomes second last and so on.



arr = [4,5,1,2] 
return_arr = []

for i in range(len(arr)-1,-1,-1):
    return_arr.append(arr[i])

#print(return_arr)


#Time complexity O(n) Space complexity O(n)

#Second approach
# Two pointers maybe

left = 0
right = len(arr) - 1
temp = 0
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
print(f"after {arr}")
'''
# Time Complexity O(n/2) -> O(n)  / Space Complexity O(1)


# Rotate an Array - Clockwise or Right

#Naive approach
'''
arr = [1,2,3,4,5,6]

for _ in range(3):
    last = arr[len(arr)-1]
    for i in range(len(arr)-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = last

#print(f"after {arr}")
'''
#Using Temporary arr
'''
arr = [1, 2, 3, 4, 5, 6]
d = 2
d %= len(arr)
print(arr)

arr[0:d] = arr[-d:]
arr[d:] = arr[:-d]
print(arr)
'''
#arr = [1, 2, 3, 4, 5, 6]
#print(arr[-2:]) # get this element by starting that position which is -2 ->  0  1  2  3  4  5
      #                                                                   -> -6 -5 -4 -3 -2 -1 
#print(arr[:-2]) # get until this element based on the current index which is given
#print(arr[4:-1])

from ast import List


arr = [1, 2, 3, 4, 5, 6]
d = 2
return_arr = [0] * len(arr)
for i in range(len(arr)-1,-1,-1):
    return_arr[(i +d) % len(arr)] = arr[i]

#print(return_arr)

# Time O(n) Space O(n)
'''
arr2 = [1, 2, 3, 4, 5, 6]
k = 2
k = k % len(arr2)
l, r = 0, len(arr2) - 1
print(arr2)
while l < r:
    arr2[l], arr2[r] = arr2[r], arr2[l]
    l, r = l+1 , r-1 

# [6,5,4,3,2,1]
l, r = 0, k - 1
while l < r:
    arr2[l], arr2[r] = arr2[r], arr2[l]
    l, r = l+1 , r-1 

# [5,6,4,3,2,1]

l, r = k, len(arr2) - 1
while l < r:
    arr2[l], arr2[r] = arr2[r], arr2[l]
    l, r = l+1 , r-1 
 
print(arr2)
'''

'''
hash_set = set()
hash_set.add(2)
hash_set.add(2)
hash_set.add(2)
hash_set.add(2)

print(hash_set)
'''
class Solution:
        
    def isSubset(self, a : list[int],b : list[int]) -> bool:
        
        hash_set = set(a)
        for num in b:
            if num not in hash_set:
                return False
        return True

    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

        An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
        '''
        hash_map_s = {}
        hash_map_t = {}

        if len(s) != len(t):
            return False
        for i in range(len(s)):
            hash_map_s[s[i]] = 1 + hash_map_s.get(s[i],0)
            hash_map_t[t[i]] = 1 + hash_map_t.get(t[i],0)
        
        for c in hash_map_s:
            print(c)
            if hash_map_s[c] != hash_map_t.get(c,0):
                return False
        return True
        #return True if hash_map_s == hash_map_t else False

    def isAnagramSorted(self, s: str, t: str) -> bool:
        return True if sorted(s) == sorted(t) else False
    
    def bubble_sort(self, arr : list[int]) -> list[int]: #numbers = [64, 34, 25, 12, 22, 90, 11]
        for i in range(len(arr)):
            for j in range(0,len(arr)-1-i):
                print(f"iterations {j}")
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
    
    def sortString(self, a: str) -> str:
        ascii_values = [ord(char) for char in a]
        ascii_values_sorted = self.bubble_sort(ascii_values)
        return "".join([chr(ascii_val) for ascii_val in ascii_values_sorted])
    
    def isAnagramAlternative(self, s: str, t: str) -> bool:
        return True if self.sortString(s) == self.sortString(t) else False


    def test_bubble_sort(self,a : list[int]) -> str: # a = [-5,3,2,1,-3,-3,7,2,2]
        flag = True
        while flag:
            flag = False
            for j in range(1,len(a)):
                if a[j-1] > a[j]:
                    flag = True
                    a[j-1],a[j] = a[j], a[j-1]
                    
        return a
    

    def sort_for_two_sum(self, a : list[int]) -> list[int]:
        flag = True
        while flag:
            flag = False
            for i in range(len(a)):
                if a[i-1] > a[i]:
                    flag = True
                    a[i-1],a[i] = a[i], a[i-1]
        return a
    
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        sorted_nums = self.sort_for_two_sum(nums)
        left,right = 0, len(sorted_nums)-1
        return_list = []
        for i in range(len(sorted_nums)):
            if arr[left] + arr[right] == target:
                return_list.append(left,right)
            if arr[left] + arr[right] > target:
                left += 1
            else: right -= 1

        return return_list

    def twoSumAgain(self, nums: List[int], target: int) -> List[int]: # nums = [2,7,11,15] target=9
        hash_map = {}
        for ix,val in enumerate(nums):
            if target - nums[i] not in hash_map:
                hash_map[nums[ix]] = ix
            else:
                return [hash_map[target - nums[ix]],ix]
            
def main():

    solution_Ex = Solution()
    #print(solution_Ex.isSubset(a,b))
    #print(solution_Ex.isAnagram(s = "jar", t = "jam"))
    #print(solution_Ex.isAnagramSorted(s = "jar", t = "jam"))
    #print(solution_Ex.isAnagramAlternative(s="abcdefasd",t="abcdefasdasd"))
    #print(solution_Ex.test_bubble_sort(a = [-5,3,2,1,-3,-3,7,2,2]))
    print(solution_Ex.twoSumAgain(nums=[3,4,5,6],target=7))
main()
