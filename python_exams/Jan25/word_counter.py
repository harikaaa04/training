"""
Word Counter
- Create a program to count the occurrences of each word in a sentence provided by the
user.
"""

def word_counter(sent):
    """Counts the number of words in a sentence"""
    words = sent.split()
    count = len(words)
    return count

def main():
    sentence = input("Enter a sentence: ")
    count = word_counter(sentence)
    print(f"There are {count} words in this sentence")

main()