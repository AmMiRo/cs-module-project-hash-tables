# Your code here
# Read in all the words in one go
with open("robin.txt") as f:
    words = f.read()

length = 0
words_dic = {}
forbidden_char = ["\"", "\\", ":", ";", ",", ".", "-", "+", "=", "/", "|", "[", "]", "{", "}", "(", ")",  "*", "^", "&"]
for char in forbidden_char:
    words = words.replace(char, "")
words = words.replace("\n", " ")
words_arr = words.split(" ")
for word in words_arr:
    word = word.lower()
    if len(word) > 1:
        if len(word) > length:
            length = len(word)
        if word in words_dic:
            words_dic[word] -= 1
        else:
            words_dic[word] = -1
tuple_arr = list(words_dic.items())
tuple_arr.sort(key=lambda tuple: (tuple[1], tuple[0]))
solution = ""
for tup in tuple_arr:
    solution += tup[0].ljust(length + 1) + "#" * abs(tup[1]) + "\n"
 
print(solution)