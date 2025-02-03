def isPalindrome(s):
    return s == s[::-1]

def longestPalindrome(arr):
    if not arr:
        return ""  
    longest_pal = ""
    for i in arr:
        if isPalindrome(i) and len(i) > len(longest_pal):  # Compare with len(longest_pal)
            longest_pal = i
    return longest_pal

palindromes = [
    "madam", "hello", "racecar", "python", "level", "world", "radar", "apple", 
    "rotor", "banana", "civic", "orange", "deified", "computer", "noon", 
    "table", "refer", "chair", "kayak", "guitar", "malayalam"
]

print("Longest palindrome:", longestPalindrome(palindromes))