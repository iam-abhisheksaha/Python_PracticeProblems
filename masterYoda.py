
# MASTER YODA: Given a sentence, return a sentence with the words reversed

def reverse_word(string):
    return " ".join(string.split()[::-1])

print(reverse_word('macdonald is good'))