# For this practice problem, write a program that outputs The Flintstones Rock! 10 times, with each line indented 1 space to the right of the line above it. The output should start out like this:

# The Flintstones Rock!
#  The Flintstones Rock!
#   The Flintstones Rock!
#    ...

# phrase = 'The Flintstones Rock!'
# padding = ''
# for line in range(1, 11):
#     if line == 1:
#         print(phrase)
#     else:
#         padding += ' '
#         print(padding + phrase)

# for padding in range(1, 11):
#     print(" " * padding + "The Flintstones Rock!")

# def factors(number):
#     # assert number > 0, 'input is less than 0'
#     divisor = number
#     result = []
#     while divisor > 0:
#         if number % divisor == 0:
#             result.append(number // divisor)
#         divisor -= 1
#     return result
# print(factors(-1))
# print(factors(10))

# def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
#     buffer.append(new_element)
#     if len(buffer) > max_buffer_size:
#         buffer.pop(0)
#     return buffer

# def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
#     buffer = buffer + [new_element] # concatenates elements, same as appending 
#     if len(buffer) > max_buffer_size:
#         buffer.pop(0)
#     return buffer

# def new_list_creator(new_list):
#     new_list = new_list
#     return new_list

# original_list = [1, 2]
# second_list = new_list_creator(original_list)
# print(original_list)
# print(second_list)
# print(original_list == second_list)
# print(original_list is second_list)

# print(0.3 + 0.6) # 0.9
# print(0.3 + 0.6 == 0.9) # True

# nan_value = float("nan")
# # print(nan_value)
# # print(nan_value == float("nan")) # TypeError, cannot coerce a string into a float
# import math
# print(math.isnan(nan_value))

# answer = 42

# def mess_with_it(some_number):
#     return some_number + 8

# new_answer = mess_with_it(answer)

# print(answer - 8) # 34

# One day, Spot was playing with the Munster family's home computer, and he wrote a small program to mess with their demographic data:

# munsters = {
#     "Herman": {"age": 32, "gender": "male"},
#     "Lily": {"age": 30, "gender": "female"},
#     "Grandpa": {"age": 402, "gender": "male"},
#     "Eddie": {"age": 10, "gender": "male"},
#     "Marilyn": {"age": 23, "gender": "female"},
# }

# def mess_with_demographics(demo_dict):
#     for key, value in demo_dict.items():
#         value["age"] += 42
#         value["gender"] = "other"

# mess_with_demographics(munsters) # mutates munsters because munsters contains pointers to other dicts as the corresponding values for each item in the dict.

# def rps(fist1, fist2):
#     if fist1 == "rock":
#         return "paper" if fist2 == "paper" else "rock"
#     elif fist1 == "paper":
#         return "scissors" if fist2 == "scissors" else "paper"
#     else:
#         return "rock" if fist2 == "rock" else "scissors"
    
# print(rps(rps(rps("rock", "paper"), rps("rock", "scissors")), "rock"))

# rps("paper", "rock") # "paper"

# def foo(param="no"):
#     return "yes"

# def bar(param="no"):
#     return param == "no" and foo() or "no"

# bar(foo())

# foo() evaluates to "yes". we pass "yes" to invoking bar("yes"). 
# param == "no" evaluates to False
# False and foo() evaluates to False because only the left operand evaluates due to short circuiting
# False or "no" then evaluates to "no"

a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))