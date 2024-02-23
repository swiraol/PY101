# Will the code below raise an error?

# numbers = [1, 2, 3]
# numbers[6] = 5

# No, it'll add the value 5 to the corresponding index, 6

# How can you determine whether a given string ends with an exclamation mark (!)?

# str1 = "Come over here!"  # True
# str2 = "What's up, Doc?"  # False

# print(str1[len(str1) -1] == '!')
# print(str2[len(str2) -1] == '!')

# famous_words = "seven years ago..."

# Show two different ways to put the expected "Four score and " in front of it.

# 1

# print('Four score and ' + famous_words)

# # 2

# print(f'Four score and {famous_words}')

# Using the following string, create a new string that contains all lowercase letters except for the first character, which should be capitalized.

# munsters_description = "the Munsters are CREEPY and Spooky."
# => 'The munsters are creepy and spooky.'

# munsters_description = munsters_description[0].upper() + munsters_description[1:]

# print(munsters_description)

# Return a new string that swaps the case of all of the letters:

# munsters_description = "The Munsters are creepy and spooky."

# "tHE mUNSTERS ARE CREEPY AND SPOOKY."

# print(munsters_description.swapcase())

# Determine whether the name Dino appears in the strings below -- check each string separately:

# str1 = "Few things in life are as important as house training your pet dinosaur."
# str2 = "Fred and Wilma have a pet dinosaur named Dino."

# print('Dino' in str1)
# print('Dino' in str2)

# How can we add the family pet, "Dino", to the following list?

# flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]

# flintstones.append('Dino')

# In the previous problem, our first answer added 'Dino' to the list like this:

# flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
# flintstones.append("Dino")
# print(flintstones + ['Dino', 'Hoppy'])

# How can we add multiple items to our list (e.g., 'Dino' and 'Hoppy')? Replace the call to append with another method invocation.

# Return a new version of this sentence that ends just before the word house. Don't worry about spaces or punctuation: remove everything starting from the beginning of house to the end of the sentence.

# advice = "Few things in life are as important as house training your pet dinosaur."
# Expected return value:
# => 'Few things in life are as important as '
# index = advice.find('house')
# print(advice[:index])

# Replace the word "important" with "urgent" in this string:

advice = "Few things in life are as important as house training your pet dinosaur."

advice = advice.replace('important', 'urgent')
print(advice)