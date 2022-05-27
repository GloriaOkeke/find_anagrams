# Check if a word is an anagrams 
# Example:
# find_anagrams("hello", "") --> False
# find_anagrams("racecar") --> True


def is_anagram(a, b):
   str1=a.replace(" ", "")
   str2=b.replace(" ", "")   
   if (sorted(str1) == sorted(str2)):
      return True
   else:
      return False
print(is_anagram('break', 'rear'))        