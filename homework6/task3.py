# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

from f import input_two_num as two

nums = two()
contains_square = lambda nums: nums[0] == nums[1] ** 0.5 or nums[1] == nums[0] ** 0.5

print(contains_square(nums))