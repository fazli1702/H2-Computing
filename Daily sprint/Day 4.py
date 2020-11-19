def reverse(string):
    return string[::-1]

def largest(n):
    palindrome = []
    for i in range(n):
        for j in range(n):
            if str((i*j)) == reverse(str((i*j))):
                palindrome.append(i*j)
            else:
                continue

    return max(palindrome)

print(largest(100))
print(largest(300))
print(largest(500))
