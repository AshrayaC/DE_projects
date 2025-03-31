
def check_palindrome(str):
    rev_str = ""
    rev_str = str[::-1]
    print(rev_str)
    if rev_str.lower() == str.lower():
        return True
    else:
        return False
    
str = "rar"
print(check_palindrome(str))