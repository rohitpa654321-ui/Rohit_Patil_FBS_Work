### Q. Python Program to Calculate the Number of Words and the Number of Characters Present in a String.


str = input("Enter a string: ")

word = str.split()

word_count = len(word)
chr_count = len(str)

print("Number of words : ", word_count)
print("Number of characters : ", chr_count) 