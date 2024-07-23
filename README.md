# Explanaition of my programs from leetcode and codeblocks
My code wars programs with descriprions and my way of thinking

## 1.  Build a pile of Cubes (.py)

### 1.1 Task
"Our construct a building which will be a pile of n cubes. The cube at the bottom will have a volume of n^3, the cube above will have volume of (n-1)^3 and so on until the top which will have a volume of 1^3."
### 1.2 Link 
link : https://www.codewars.com/kata/5592e3bd57b64d00f3000047/train/pythonour 
## 2. Count IP Addresses (.py)
### Task:
"Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).
All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one."

### Solution 
To solve this problem, you need to convert the IPv4 addresses to their numerical equivalents, then calculate the difference between them.

Steps:
* Convert an IPv4 address to a numerical value:

* Split the address into its four octets.
Each octet is an 8-bit number, so combine them into a 32-bit number.
* For example, the IP "192.168.1.1" can be converted to a numerical value by computing:

```python
192 * 256^3 + 168 * 256^2 + 1 * 256^1 + 1 
```
 
* Compute the difference between the two numerical values.

### Link:
https://www.codewars.com/kata/526989a41034285187000de4/train/python
## 3. Two sums
### Task:
"Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice."
### Solution:
-Create an empty dictionary to store the indices of the numbers we have seen so far.
-Iterate through the list of numbers using their indices.
-For each number, calculate its complement (target - number).
-Check if the complement exists in the hash map.
-If it exists, return the indices of the complement and the current number.
-If it does not exist, store the current number and its index in the hash map.
-If no solution is found by the end of the iteration, return an empty list (this shouldn't happen as per the problem statement).
### Link:
https://leetcode.com/problems/two-sum/submissions/1322741573/
## 5. Reverse int
### Task:
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
### Solution:

 use a loop to repeatedly extract the last digit of x and build the reversed number.
After extracting each digit, I reduced x by removing its last digit.
### Link:
https://leetcode.com/problems/reverse-integer/


## 2418. Sort the People
### Task: 
"You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n, For each index i, names[i] and heights[i] denote the name and height of the ith person.
Return names sorted in descending order by the people's heights."
### Solution:
* zip-ing: glue both arrays '[height, name]' and sort them by higher int,
* sorting: we sort the zipings starting from first element which is ''height'' as function 'lambda x: x[0]' gives me the number which is used as a " sorting key" 
*  unziping: "sorted_names = [name for height, name in sorted_people] "we unzip this sorted package  to get our list of names 
### Link:
https://leetcode.com/problems/sort-the-people/description/?envType=daily-question&envId=2024-07-22


## 601. Human Traffic of Stadium
### Task: 
Write a solution to display the records with three or more rows with consecutive id's, and the number of people is greater than or equal to 100 for each.
Return the result table ordered by visit_date in ascending order.
The result format is in the following example.
### Solution:
i explain later [never]
### Link:
https://leetcode.com/problems/human-traffic-of-stadium/description/?lang=pythondata

# link do my leetcode account
https://leetcode.com/u/kitajussus/
# link do my code wars account
https://www.codewars.com/users/kitajusSus


## TEMPLATE
### Task:
### Solution 
### Link:
