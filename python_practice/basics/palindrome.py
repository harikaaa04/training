def is_palindrome2(s):
    """Using list and 2 pointerss"""
    l = list(s.lower())
    n = len(l)
    for i in range(n//2 + 1):
        if l[i] != l[-i-1]:
            return False 
    return True 

def is_palindrome(s):
    """Using string reversal"""
    return s == s[::-1]

def get_words(s):
    """Gets words from a sentence"""
    words, word = [], ''
    for ch in s:
        if ch == ' ' and word != '':
            words.append(word)
            word = ''
        elif ch != ' ':
            word += ch 
    if word != '':
        words.append(word)
    return words

def palindromic_words(words):
    """Returns palindromic words from a list of words"""
    pal_words = []
    for word in words:
        if is_palindrome(word):
            pal_words.append(word)
    return pal_words

def main():
    s = input("Enter a string: ")

    words = get_words(s)
    pal_words = palindromic_words(words)
    print("The palindromic words in the sentence are:", pal_words)

    
    # if is_palindrome(s):
    #     print(f"{s} is a palindrome")
    # else:
    #     print(f"{s} is not a palindrome")


main()

