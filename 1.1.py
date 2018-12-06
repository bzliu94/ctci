# 2018-12-06

# problem 1.1

# implement an algorithm to determine if a string has all unique characters

# what if you cannot use additional data structures?

def strHasAllUniqueChars(curr_str):
  str_char_set = set(list(curr_str))
  if len(str_char_set) < len(list(curr_str)):
    return False
  else:
    return True

str1 = ""
str2 = "abcdee"
str3 = "abcdef"

print strHasAllUniqueChars(str1)
print strHasAllUniqueChars(str2)
print strHasAllUniqueChars(str3)


