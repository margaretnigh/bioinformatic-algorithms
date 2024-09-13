textf = "GAGT T AACGAACGCT T AACT G"
k = 3

def isPalindrome(s):
    return s == s[::-1]

def findPalindromes(text, k):
    text = text.replace(" ", "")
    minLength = k
    palindromes = []
    if len(text) < minLength:
        return
    for i in range(len(text) - minLength + 1):
        substring = text[i:i + minLength]
        if isPalindrome(substring):
            palindromes.append(substring)
    return palindromes

allPalindromes = findPalindromes(textf, k)
print(*allPalindromes) 