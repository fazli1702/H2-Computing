def is_palindrome(string):
    if string[::-1] == string:
        return True
    return False


print(is_palindrome('kayak'))
print(is_palindrome('reviver'))
print(is_palindrome('christmas'))
