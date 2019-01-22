# A few simple functions to play with strings.


def pig_latin(word):
    return word[1:]+word[0]+"ay"


def count_vowels(word):
    a = ("a", "e", "i", "o", "u", "y")
    counter = 0
    for x in word:
        if x in a:
            counter += 1
    return counter


def is_palindrome(word):
    return word == word[::-1]


def count_words(file_name):
    f = open(file_name, "r")
    text = f.read()
    return len(text.split(" "))


word = input("Please enter a word: ")

print("Pig Latin: ", pig_latin(word))
print("Vowels counter: ", count_vowels(word))
print("is palindrome?: ", is_palindrome(word))
file = "file.txt"
print("Words counter from text file: ", count_words(file))
