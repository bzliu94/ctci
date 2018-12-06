# 2018-12-06

# problem 1.3

# given two strings, write a method to decide if one is a permutation of the other

from collections import defaultdict

def strIsPermutationOfOtherStr(str1, str2):
  char_to_count_dict1 = defaultdict(lambda: 0)
  char_to_count_dict2 = defaultdict(lambda: 0)
  char_list1 = list(str1)
  for curr_char in char_list1:
    char_to_count_dict1[curr_char] += 1
  char_list2 = list(str2)
  for curr_char in char_list2:
    char_to_count_dict2[curr_char] += 1
  k_v_pairs1 = char_to_count_dict1.items()
  k_v_pairs2 = char_to_count_dict2.items()
  for curr_k_v_pair in k_v_pairs1:
    curr_key, curr_value = curr_k_v_pair
    if char_to_count_dict2[curr_key] != curr_value:
      return False
  for curr_k_v_pair in k_v_pairs2:
    curr_key, curr_value = curr_k_v_pair
    if char_to_count_dict1[curr_key] != curr_value:
      return False
  return True

str1_1 = "abcd"
str1_2 = "bacd"
print strIsPermutationOfOtherStr(str1_1, str1_2)

str2_1 = "abc"
str2_2 = ""
print strIsPermutationOfOtherStr(str2_1, str2_2)

str3_1 = ""
str3_2 = "abc"
print strIsPermutationOfOtherStr(str3_1, str3_2)

str4_1 = ""
str4_2 = ""
print strIsPermutationOfOtherStr(str4_1, str4_2)

str5_1 = "hello"
str5_2 = "ohell"
print strIsPermutationOfOtherStr(str5_1, str5_2)

str6_1 = "hellothere"
str6_2 = "hello"
print strIsPermutationOfOtherStr(str6_1, str6_2)

str7_1 = "hellothere"
str7_2 = "therehello"
print strIsPermutationOfOtherStr(str7_1, str7_2)


