word = input('Want to see if it is a palindrome? Enter the Word : ') 
def is_palindrome(word): 
    if len(word) <= 2:
        return True
    elif word[0] == word[-1]: 
        return is_palindrome(word[1:-1])
    else: 
        return False
    
print(is_palindrome(word))