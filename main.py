# Check if a word is an anagrams 
# Example:
# find_anagrams("hello", "") --> False
# find_anagrams("racecar") --> True


# str1= input("Enter string 1: ")
# str2= input("Enter string 2: ")
# str1_list =list(str1)
# str1_list.sort()
# str2_list= list(str2)
# str2_list.sort()

# if len(str1_list)==len(str2_list):

#    if str1_list==str2_list: 
#       print("True")
#    else:
#     print("False")
# else:
#     print("False") 
   

# def is_anagram(rear, rare):
#    list1=list(rear)
#    list2=list(rare)
#    list1.sort()
#    list2.sort()
#    return(list1 == list2)

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)
print(is_anagram('rare', 'rear'))    
