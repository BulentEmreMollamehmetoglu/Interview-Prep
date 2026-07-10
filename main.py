import math
import re
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
from inspect import stack
from typing import Deque


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
from collections import deque
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

    def bubble_sort_group_anagrams(self,a :list[int]) -> list[int]: # bac
        flag = True
        while flag:
            flag = False
            for i in range(1,len(a)):
                if a[i] < a[i-1]:
                    flag = True
                    a[i-1] , a[i] = a[i], a[i-1]
        return a
    
    def sortForGroupAnagrams(self,strs) -> str:
        ascii_values = [ord(ascii) for ascii in strs]
        sorted_ascii = self.bubble_sort_group_anagrams(ascii_values)
        return "".join([chr(one_ascii) for one_ascii in sorted_ascii])
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strs = ["act","pots","tops","cat","stop","hat"]
        hash_map = {} # keys,values -> sorted(strs[i]) : [strs[i]]
        for i in range(len(strs)):
            if self.sortForGroupAnagrams(strs[i]) in hash_map:
                hash_map.get(self.sortForGroupAnagrams(strs[i])).append(strs[i])
            else: hash_map[self.sortForGroupAnagrams(strs[i])] = [strs[i]]
        return list(hash_map.values())
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strs = ["act","pots","tops","cat","stop","hat"]
        hash_map = {} # keys,values -> sorted(strs[i]) : [strs[i]]
        for i in range(len(strs)):
            if "".join(sorted(strs[i])) in hash_map: 
                hash_map.get("".join(sorted(strs[i]))).append(strs[i])
            else: hash_map["".join(sorted(strs[i]))] = [strs[i]]
        return list(hash_map.values())
        # sorted O(m * nlogn) m len of str and n chars inside of the strs[i]
        # O(k) space complexity 
    def groupAnagramsAlternative(self, strs: List[str]) -> List[List[str]]:
        # strs = ["act","pots","tops","cat","stop","hat"]
        hash_map = {}
        count = [0] * 26
        for i in range(len(strs)):
            for j in range(len(strs[i])):
                count[ord(strs[i][j]) - ord('a')] += 1
            tuple_count = tuple(count)
            if tuple_count not in hash_map:
                hash_map[tuple_count] = [strs[i]]
            else:
                hash_map.get(tuple_count).append(strs[i])
            count = [0] * 26
        return list(hash_map.values())
        # Time : O(n * k)
        # Space : O(n * k) -> (n) n: size of the hash_map O(26 * n) -> O(n)

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        '''
        I need to find the variables that are most occurent.
        I need to check the elements and how many times they occur in the particular list
        I can make a list about themselves and how many times they occur.
        That list could be a hashmap because it stores the keys which are going to be in that case 
        the values itself and the values are going to be how many times they occur. 
        But the problem is how can i find the bigger value in the hashmap
        Maybe I can use a dict comprehension.
        I just need to sort the hash_map. How can i sort the hash_map

        Time and space complexities are Time: O(n) Space : O(n)

        Can I use that K value as a delimiter. And return the list as a list[-2:]

        After solution:

        Let's assume n = 6 which is len of the arr
        m = len of hash_map because hash_map only contains unique elements
        First for loop
        Time : O(n)
        Space : O(m)

        Sorted:

        Sort only goes for hash_map so it needs to be
        Time: O(m logm)
        Space: O(m) sorting creates a list

        Return last k:
        Time: O(m + k)
        Space : O(m)

        Total:
        Time: O(n + m logm)
        Space : O(m)
        '''
        hash_map = {}
        for i in nums:
            hash_map[i] = 1 + hash_map.get(i,0)

        sorted_hash_map = {k : v for k,v in sorted(hash_map.items(),key= lambda item: item[1])}
        return list(sorted_hash_map.keys())[-k:]

        # Solve the same problem with heap and 
        # neetcode solution
    
    def topKFrequentAlternative(self, nums: list[int], k: int) -> list[int]:
        # [1,2,2,3,3,3]
        '''
        values 1 2 3 4 5 6
        keys   []
        '''
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        for n,v in count.items():
            freq[v].append(n)

        res = []
        examp = []
        print(freq)
        examp.append(freq[-1][0])
        print(examp)
       
        for i in range(len(freq) -1 ,0 , -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res

    def isPalindrome(self, string: str) -> bool:
        '''
        a palindrome
        String that is equals forwards and backwards.
        We need to use alphanumeric characters. (A-a)(Z-z)(0-9)
        no melon!
        '''

        # to check  isalnum()

        # remove invalid characters from str
        
        # strs[::-1].strip() check reverse = forward
        
        string = ("".join([char for char in string if char.isalnum()])).strip()
        return True if string.lower()==string[::-1].lower() else False
    
        # Time O(n) Space O(n)
    
    def isPalindromeTwoPointers(self, s:str) -> bool:
        # s = ".,"
        left,right = 0, len(s)-1
        while left < right:
            while left < right and not self.isAlnumNotBuiltIn(s[left]):
                left += 1
            while right > left and not self.isAlnumNotBuiltIn(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower() : return False 

            l, r = l+1 , r-1
        return True
        # Time: O(n) Space: O(1)

    def isAlnumNotBuiltIn(self, char : chr) -> bool:
        #Check digits
        return (ord('0') <= ord(char) <= ord('9') or 
                ord('a') <= ord(char) <= ord('z') or 
                ord('A') <= ord(char) <= ord('Z'))
    '''
    input : num: list[int] -> non-decreasing order
    output : [index1,index2] , ix1 + ix2 = target , ix1 < ix2 , ix1 != ix2, 
    no same elements for ix1 and ix2

    one valid solution exists
    solution must use O(1) space
    ''' 

    def twoIntegerSum(self,nums : list[int] , target : int) -> list[int]:
        '''
        left, right
        left < right , left != right
        I can't use hashmap.
        nums = [1,2,3,4] ->  5
        '''
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
    
    def twoIntegerSumAlternative(self, nums: list[int] , target: int) -> list[int]:
        l,r = 0, len(nums) - 1
        while l < r :
            curSum = nums[l] + nums[r]
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l+1,r+1]
            
    def stackDS(self):
        stack = []
        stack.append(5)
        stack.append(4)
        stack.append(3)
        print(stack)
        print(stack[-1])
        print(stack.pop())
        print(stack.peek())
    
    def queues(self):
        q = Deque()
        print(q)
        q.append(5)
        q.append(6)
        print(q)
        print(q.popleft())


    '''
    '(',')','{','}','[',']'
    
    input string is valid: 
    1. every open bracket should be closed with the same type of close bracket.
    2. open brackets should be closed in the correct order.
    3. every close bracket should have a corresponding open bracket of the same type.

    return true if string is valid , otherwise false
    input -> true -> s = "()" , s = "()[]" , s = "{[()]}"
    false -> s = "[(])"
    '''
    def isValidString(self, s : str) -> bool:
        hash_map = {")" : "(" , "]" : "[" , "}" : "{"}
        stack = []
        for i in s:
            if i in hash_map:
                if stack and hash_map[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return False if stack else True 
    
    def checkStackIsEmpty(self) -> bool:
        stack = [1,2,3,4]
        return True if stack else False

    '''
    design a stack class
    push
    pop
    top 
    getMin

    MinStack -> initializes the stack object
    push method takes an element "val" onto the stack
    -> is val always a int or string?
    pop method removes the element on the top of the stack
    -> is this stack always going to has some kind of elements
    top method gets the top element of the stack
    -> is this stack always going to has some kind of elements
    getMin -> retrieves the minimum element in the stack

    Each function should run in O(1) time. 

    pop, top and getMin will always be called on non-empty stacks.
    '''


    def evalRPN(self, tokens : list[str]) -> int:
        stack = []
        operations = ["+", "-","*","/"]
        for i in tokens:
            if i not in operations:
                stack.append(i) 
            else:
                val1,val2 = int(stack.pop()) , int(stack.pop())
                if i == "+":
                    stack.append(val2 + val1)
                elif i == "-":
                    stack.append(val2 - val1)
                elif i == "*":
                    stack.append(val2 * val1)
                elif i == "/":
                    stack.append(val2 / val1)
        return int(stack.pop())
    
        '''
    arr[int] -> temperatures
    temperatures[i] -> stands for daily temperature on the day i.

    return -> result[] -> result[i] -> return the number of days if a future day's temperature
    is warmer than yesterday.

    temperatures = [30,38,30,36,35,40,28]
    
    '''

    def dailyTemperatures(self, temperatures : list[int]) -> list[int]:
        #temperatures = [30,38,30,36,35,40,28]
        result = []
        count = 0
        for i in range(len(temperatures) - 1):
            for j in range(i+1,len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    count = j - i
                    break
            result.append(count)
            count = 0
        result.append(0)
        return result
    
    def dailyTemperatureStack(self, temperatures : list[int]) -> list[int]:
        #temperatures = [30,38,30,36,35,40,28]
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                old_index = stack.pop()
                result[old_index] = i - old_index
            stack.append(i)
        return result
    '''
    [-,-,-,-,-,-,-,-] the len of [] is n

    input -> position[int] , speed[int] both of length n

    position[i] -> position of the ith car.
    speed[i] -> speed of the ith car.
    target -> int

    stack = []
    num_of_car = len(position)
    return_val = 0
    j = 0
    flag = True
    target_position = [] * len(position)
    while flag:
        est_target = position[j] + ((j+1)  * speed[j]) # 4 6
        target_position[j] = est_target
        if not stack and est_target not in stack:
            stack.append(est_target)

        if stack and stack[-1] == est_target:
            
            
        while stack and stack[-1] == est_target and est_target == target:
            popped_val = stack.pop()
            return_val += 1
            num_of_car -= 1
        j += 1
        if num_of_car == 0:
            flag = False
    '''

    '''
    Second thoughts
    
    x = v.t
    arrival_time = (target - position) / speed = t
    0 -> 3
    1 -> 3

    
    3
    5 -> rounded up
    10
    3
    stack = []
    max_time = 0
    fleet = 0
    for i in range(len(position)):
        arrival_time = (target - position[i]) / speed[i]
        if not stack:
            stack.append(arrival_time)
            max_time = arrival_time
            fleet += 1
        if stack and max_time < arrival_time:
            stack.pop()
            stack.append(arrival_time)
            max_time = arrival_time
            fleet += 1
        
    '''

    def carFleet(self,target : int, position : list[int] , speed: list[int]) -> int:
        # (target = 10, position=[6,8], speed=[3,2]))
        fleet = 0
        slowest_time = 0
        hash_map = {}
        for i,j in zip(position,speed):
            hash_map[(i,j)] = (target - i) / j
        hash_map = sorted(hash_map.keys(), key= lambda item : item[0],reverse=True)
        for i,j in hash_map:
            time = (target - i) / j
            if slowest_time < time : 
                fleet += 1
                slowest_time =  time

        return fleet

    def carFleetAlternative(self,target : int , position : list[int], speed : list[int]) -> int:
        #target = 10, position=[4,1,0,7], speed=[2,2,1,1]
        #target=10 position=[1,4] speed=[3,2]
        stack = []
        cars = [(positions,speeds) for positions,speeds in zip(position,speed)]
        sorted_cars = sorted(cars, key = lambda positions : positions[0],reverse=True)
        print(sorted_cars)
        for i,j in sorted_cars:
            time = (target - i) / j
            print(time)
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
    '''
    nums : list[int] -> list[list[int]]
    no duplicate triplets
    '''

    def threeSum(self, nums : list[int]) -> list[list[int]]:
        # [1,0,-1,2,-1,-4] -> [[1,0,-1],[-1,-1,2]]
        # sort -> [-4,-1,-1,0,1,2]
        sorted_nums = sorted(nums)
        return_list = []
        for i in range(len(sorted_nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            l,r = i + 1, len(sorted_nums) - 1
            while l < r :
                current_sum = sorted_nums[i] + sorted_nums[l] + sorted_nums[r]

                if current_sum < 0:
                    l += 1
                elif current_sum > 0 :
                    r -= 1
                else:
                    return_list.append([sorted_nums[i],sorted_nums[l],sorted_nums[r]])
                    l += 1
                    r -= 1

                    while l < r and sorted_nums[l] == sorted_nums[l-1]:
                        l += 1
                    
                    while l < r and sorted_nums[r] == sorted_nums[r+1]:
                        r -= 1

        return return_list
        






    def threeSumAlternative(self,nums : list[int]) -> list[list[int]] :
        # [1,0,-1,2,-1,-4] -> [[1,0,-1],[-1,-1,2]]
        # sort -> [-4,-1,-1,0,1,2]
        return_list = []
        nums.sort() # creates O(1) space in the memory. 
        for i in range(len(nums)):
            l,r = i+1, len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while l < r :
                sum = nums[l] + nums[r] + nums[i]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    return_list.append([nums[l],nums[r],nums[i]])
                    l += 1 
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return return_list

    '''
    Time : O(n logn)  + O(n^2) Space : O(1) 
    '''


    '''
    heights : list[int]


    '''
    def maxArea(self,heights : list[int]) -> int :
        maxArea = 0
        l,r = 0 , len(heights) - 1
        flag = True
        while flag:
            if l == r :
                break
            area = (r -l) * min(heights[l],heights[r])

            if heights[l] < heights[r]:
                l +=1
            else:
                r -= 1
            if area > maxArea:
                maxArea = area 
        return maxArea
                

    def maxAreaAlternative(self, heights: list[int]) -> int:
        # heights = [1,7,2,5,4,7,3,6]
        l,r = 0 , len(heights) - 1
        maxArea = 0
        while l < r:         
            area = (r - l) * min(heights[l],heights[r])
            maxArea = max(area,maxArea)
            if heights[l] < heights[r] :
                l += 1
            else:
                r -= 1

        return maxArea
    
    def binarySearch(self,nums: list[int],target : int) -> bool:
        l,r = 0 , len(nums) - 1
        while l <= r:
            M = (l + r) // 2 # L + ((R-L) // 2) to prevent integer overflow
            if nums[M] == target:
                return True

            elif target > nums[M] :
                l = M + 1
            
            else:
                r = M - 1
        
        return False



    def search(self,nums : list[int],target: int) -> int:
        l,r = 0 , len(nums) - 1
        while l <= r :
            M = (l + r) // 2
            if target == nums[M]:
                return M
            elif target > nums[M]:
                l = M + 1
            else:
                r = M - 1
        return -1

    def binarySearch(self,nums : list[int],target : int) -> int :
        l,r = 0 , len(nums) - 1
        while l <= r :
            M = (l + r) // 2 

            if target == nums[M]:
                return M

            elif target > nums[M]:
                l = M + 1
            
            else:
                r = M - 1
        return -1

    def searchMatrix(self, matrix : list[list[int]],target : int) -> bool:
        '''
            m x n 2D -> matrix : list[list[int]] , target : int 
            [[1,2,3],[4,5,6],[7,8,9]] -> each row is increasing order
            return bool

            O (log(m*n)) 
        '''
        for i in range(len(matrix)): # rows
            l,r = 0 , len(matrix[i]) - 1
            while l <= r:
                M = (l + r) // 2

                if target == matrix[i][M] : 
                    return True

                elif target > matrix[i][M] :
                    l = M + 1
                
                else : 
                    r = M - 1

        return False 
    

    def searchMatrixAlternative(self,matrix : list[list[int]],target : int) -> bool:
        # [[1,2,3],[4,5,6],[7,8,9]]
        ROWS, COLS = len(matrix) , len(matrix[0])
        top , bot = 0, ROWS -1
        while top <= bot : 
            row = (top + bot) // 2

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row -1
            else:
                break
        
        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l,r = 0, len(matrix[row])
        while l <= r:
            M = (l + r) // 2

            if target == matrix[row][M]:
                return True
        
            elif target > matrix[row][M]:
                l = M + 1
            
            else:
                r = M - 1
        return False


    '''

    '''
    def searchMatrixAlternativeSecondTime(self, matrix : list[list[int]],target : int) -> bool:
        # [[1,2,3],[4,5,6],[7,8,9]]
        #O(logm * logn) = O(logm) + O(logn)
        ROWS,COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS - 1
        while top <= bot :
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
            
        if not (top <= bot) :
            return False
        row = (top + bot) // 2
        l,r = 0, len(matrix[row]) - 1
        while  l <= r :
            M = (l + r) // 2

            if target > matrix[row][M]:
                l = M + 1
            elif target < matrix[row][M]:
                r = M - 1

            else:
                return True
        return False


    '''
    piles : list[int]
    piles[i] -> number of bananas in the ith pile. [1,4,3,2]
    
    h : int -> number of hours I have to eat all the bananas.
    
    return k -> k is my bananas per hour eating rate. 

    30 + 2 + 1.30 + 1
    1 + 2 + 2 + 1
    '''


    def minEatingSpeed(self, piles: list[int], h : int) -> int :
        l,r = 1, max(piles)
        result = r
        while l <= r :

            K = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / K)

            if hours <= h :
                result = K
                r = K - 1
            
            elif hours > h :
                l = K + 1
        return result
    









    '''
    
    
    
    
    '''
    def minEatingSpeedAlternative(self, piles : list[int],h : int) -> int :
        l, r = 1, max(piles)
        result = r
        while l <= r:
            hour = 0
            K = (l + r) // 2
            for pile in piles:
                hour += math.ceil(pile/K)
            
            if hour <= h:
                result = min(result,K)
                r = K - 1
            else:
                l = K + 1
        return result
    




    '''
    nums : list[int] : originally sorted ascending order
    1 - n times rotated.

    all elements are unique
    [1,2,3,4,5,6] -> rotated 4 
    [3,4,5,6,1,2]
    
    '''


    def findMin(self, nums : list[int]) -> int : 
        l , r = 0, len(nums) - 1
        M = 0
        while l < r :

            M = (l + r) // 2

            if nums[M] > nums[r]:
                l = M + 1
            else:
                r = M
        return nums[M]




    def findMinAlternative(self,nums: list[int]) -> int:
        # [3,4,5,6,1,2]
        # [4,5,0,1,2,3]
        l, r = 0, len(nums) - 1
        while l < r:
            M = (l + r) // 2

            if nums[M] > nums[r]:
                l = M + 1
            else:
                r = M
        return nums[r]
    '''
    Time and space complexities are :
    Time -> O(log m ) m is the size of the array
    Space -> l,r constant variables, O(1)
    '''


    def findMinAlternativeSecond(self, nums : list[int]) -> int:
        for i in nums:
            if i < len(nums) - 1 and nums[i+1] < nums[i]:
                return nums[i+1]
            else:
                return nums[0]
    


    def findMinSecond(self,nums : list[int]) -> int :
        l , r = 0, len(nums) - 1
        res = nums[0]
        while l <= r :
            if nums[l] < nums[r]:
                res = min(res,nums[l])
                break
            M = (l + r) // 2 
            res = min(res,nums[M])
            if nums[M] >= nums[l]:
                l = M + 1
            else:
                r = M - 1
        return res




    def searchBinary(self, nums: list[int], target : int) -> int:
        l , r = 0 , len(nums) - 1
        
        while l <= r :
            M = (l + r) // 2
            if target == nums[M]:
                return M

            # left half sorted
            if nums[M] >= nums[l]:
                if target > nums[M]:
                    l = M + 1
                else:
                    r = M - 1

            # right half sorted
            else:
                if target < nums[M]:
                    r = M - 1
                else:
                    l = M + 1
        return -1

        '''
        nums : list[int]
        target : int
        return : int -> index of target
        else -1
        nums = [3,4,5,6,1,2], target = 1
        nums = [4,5,6,7,8,9,1,2,3] target = 4
        I can use l & r pointers to make sure that the target
        is not in that range


        [3,4,5,6,1,2], target = 4
        '''

        
    def searchBinaryAlternative(self, nums: list[int], target : int) -> int:
        l, r = 0 , len(nums) - 1
        # nums = [4,5,6,7,8,1,2,3], target = 2
        while l <= r :
            M = (l + r) // 2

            if target == nums[M]:
                return M
            # left sorted  
            if nums[M] > nums[l]:
                if nums[l] <= target <= nums[M]:
                    r = M - 1
                else:
                    l = M + 1
            # right sortedz
            else:
                if nums[M] <= target <= nums[r]:
                    l = M + 1
                else:
                    r = M - 1

        return -1

    def duplicates(self, nums : list[int], K : int) -> bool:
        # [1,2,3,2,3,3]
        # Given an array, return true if there are two elements within a window of size k that are equal
        for L in range(len(nums)):
            for R in range(L+1, min(len(nums), L + K)):
                if nums[L] == nums[R]:
                    return True
        
        return False
        # O(n * k)

    # optimized

    # hash set

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for L in range(len(nums)):
            for R in range(L + 1, min(len(nums), L + k + 1)):
                if nums[L] == nums[R]:
                    return True
        return False
    


    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0
        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False




    def slidingWindow(self, nums : list[int] , k : int) -> bool :
        # k = 2 if are there 2 values which are the same return true otherwise false
        for L in range(len(nums)):
            for R in range(L + 1, min(len(nums), L + k)):
                if nums[L] == nums[R]:
                    return True
        
        return False



    def slidingWindow(self, nums : list[int] , k : int) -> bool:
        window = set()
        L = 0
        for R in range(len(nums)):
            if R - L > k : 
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False



    '''
    arr : list[int] , k : int , threshold : int
    return -> num of subarrays of size k and average >= threshold
    avg = sum() / len()

    '''
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        result,sum = 0,0
        for L in range(len(arr)):
            sum += arr[L]
            for R in range(L + 1, min(len(arr), L + k)):
                sum += arr[R]

            if sum / k >=  threshold:
                result += 1
            sum = 0
        return result
    # Time : O(n**2) Space : O(1)

    def numOfSubarraysOptimized(self, arr: List[int], k: int, threshold: int) -> int:
        result, avg = 0,0
        L = 0
        for R in range(len(arr)):
            avg += arr[R]
            if R - L + 1 == k:
                if avg / k >= threshold:
                    result += 1
                avg -= arr[L]
                L += 1
        return result
    
    # Time O(n) Space O(1)


    '''
    prices : list[int]
    return : int max profit
    
    [10,1,5,6,7,1]

    6
    '''

    def maxProfit(self, prices: List[int]) -> int:
        minPrice = 100
        maxProfit = 0
        for price in prices:
            minPrice = min(minPrice, price)
            profit = price - minPrice
            maxProfit = max(maxProfit,profit)
        return maxProfit




    def maxProfitSecond(self, prices : list[int]) -> int : 
        minPrice = 1000
        maxProfit = 0
        for price in range(len(prices)):
            minPrice = min(minPrice,price)
            maxProfit = max(price - minPrice,maxProfit)
        return maxProfit










def main():


    solution_Ex = Solution()
    '''
    minStack = MinStack()
    print(f"stack --> {minStack.stack}")
    minStack.push(-2);
    minStack.push(-2);
    minStack.push(-3);
    minStack.push(-3);
    print(f"stack --> {minStack.stack}")
    print(f" min stack --> {minStack.min_stack}")
    print(minStack.getMin()) 
    minStack.pop();
    print(f"stack --> {minStack.stack}")
    print(f" min stack --> {minStack.min_stack}")
    minStack.top();    
    print(f"stack --> {minStack.stack}")
    minStack.getMin(); 
    print(f"stack --> {minStack.stack}")
    '''
    #print(solution_Ex.evalRPN(tokens=["1","2","+","3","*","4","-"]))
    #print(solution_Ex.dailyTemperatures(temperatures = [30,38,30,36,35,40,28]))
    #print(solution_Ex.dailyTemperatureStack(temperatures = [30,38,30,36,35,40,28]))
    #print(solution_Ex.carFleet(target = 10, position=[6,8], speed=[3,2]))
    #print(solution_Ex.carFleetAlternative(target = 10, position=[1,4], speed=[3,2]))
    #print(solution_Ex.threeSum(nums=[-2,0,0,2,2]))
    #print(solution_Ex.threeSumAlternative(nums=[1,0,-1,2,-1,-4]))
    #print(solution_Ex.maxArea(heights = [1,7,2,5,4,7,3,6]))
    #print(solution_Ex.binarySearch(nums = [-3,1,0,1,4,7],target = 9))
    #print(solution_Ex.searchMatrix(matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15))
    #print(solution_Ex.minEatingSpeed(piles = [1,4,3,2], h = 9))
    #print(solution_Ex.minEatingSpeedAlternative(piles=[25,10,23,4], h = 4))
    #print(solution_Ex.findMin(nums=[3,4,5,6,1,2]))
    #print(solution_Ex.findMinAlternative(nums=[3,4,5,6,1,2]))
    #print(solution_Ex.searchBinary(nums=[5,1,3],target = 3))
    #print(solution_Ex.numOfSubarraysOptimized(arr=[2,2,2,2,5,5,5,8], k = 3, threshold= 4))
    print(solution_Ex.maxProfitSecond(prices=[7,6,4,3,1]))
main()




class MinStack:


    # [1,2,0]
    def __init__(self):
        self.stack = [] # initializes the stack object
        self.min_stack = []
    def push(self, val : int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)



    def pop(self) -> None:
        val = self.stack.pop()
        if self.min_stack and val < self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.min_stack:
            return self.stack[0]
        else:
            return self.min_stack[-1]