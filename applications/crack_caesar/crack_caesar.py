# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
# Read in all the words in one go
with open("ciphertext.txt") as f:
    text = f.read()

frequency_lst = ["E", "T", "A", "O", "H", "N", "R", "I", "S", "D", "L", "W", "U", "G", "F", "B", "M", "Y", "C", "P", "K", "V", "Q", "J", "X", "Z"]
letter_frequency = {}
key = {}
for char in text:
    if char.isalpha():
        if char in letter_frequency:
            letter_frequency[char] += 1
        else:
            letter_frequency[char] = 1
tuple_lst = list(letter_frequency.items())
tuple_lst.sort(key=lambda tup: tup[1], reverse=True)
for i in range(len(frequency_lst)):
    key[tuple_lst[i][0]] = frequency_lst[i]
new_str = ""
for char in text:
    if char.isalpha():
        if char in key:
            new_str += key[char]
        else:
            new_str += char
    else:
        new_str += char

print(new_str)
