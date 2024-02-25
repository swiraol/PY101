# Will the following functions return the same results?

# def first():
#     return {
#         'prop1': "hi there",
#     }

# def second():
#     return
#     {
#         'prop1': "hi there",
#     }

# print(first())
# print(second())

# What does the last line in the following code output?

# dictionary = {'first': [1]}
# num_list = dictionary['first']
# num_list.append(2)

# print(num_list) # [1, 2]
# print(dictionary) # {'first': [1, 2]}

# Given the following similar sets of code, what will each code snippet print?

# def mess_with_vars(one, two, three):
#     one = two 
#     two = three 
#     three = one 

# one = ["one"]
# two = ["two"]
# three = ["three"]

# mess_with_vars(one, two, three)

# print(f"one is: {one}") # ["one"]
# print(f"two is: {two}") # ["two"]
# print(f"three is: {three}") # ["three"]

# def mess_with_vars(one, two, three):
#     one = ["two"] 
#     two = ["three"]
#     three = ["one"]

# one = ["one"]
# two = ["two"]
# three = ["three"]

# mess_with_vars(one, two, three)

# print(f"one is: {one}") # ["one"] 
# print(f"two is: {two}") # ["two"]
# print(f"three is: {three}") # ["three"]

# def mess_with_vars(one, two, three):
#     one[0] = "two"
#     two[0] = "three"
#     three[0] = "one"

# one = ["one"] 
# two = ["two"]
# three = ["three"]

# mess_with_vars(one, two, three)

# print(f"one is: {one}") # ["two"]
# print(f"two is: {two}") # ["three"]
# print(f"three is: {three}") # ["one"]

# def is_dot_separated_ip_address(input_string): # 4.5.5
#     dot_separated_words = input_string.split(".") # ['4', '5', '5']
#     if len(dot_separated_words) < 4 or len(dot_separated_words) > 4:
#         return False
#     while len(dot_separated_words) > 0:
#         word = dot_separated_words.pop() # 4, 5, 5, 4
#         if not is_an_ip_number(word): 
#             return False

#     return True

# def is_an_ip_number(word):
#     return int(word) >= 0 and int(word) <= 255

# print(is_dot_separated_ip_address("4.5.5.256"))
# print(is_dot_separated_ip_address("4.5.5"))
# print(is_dot_separated_ip_address("4.5.5.255.255"))
# print(is_dot_separated_ip_address("4.5.5.255"))

What do you expect to happen when the greeting variable is referenced in the last line of the code below?

