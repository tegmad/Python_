def count_vowels(str) -> int:
   vowels = 'aeouyiAEOUYIO' 
   str = list(str)
   count = 0

   for i in str:
        if i in vowels:
            count+= 1

   return count

def reverse_string(str) -> str: # Hello olleH
   return str[::-1]

def is_palindrome(str):
    reversed = str[::-1]
    return reversed == str

def capitalize_string(str):
    return str.capitalize()