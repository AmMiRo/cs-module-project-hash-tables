import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
words_dic = {}
new_line = "\n"
words = words.replace(new_line, " ")
words_lst = words.split(" ")
for i in range(len(words_lst) - 1):
    if words_lst[i] in words_dic:
        if words_lst[i + 1] not in words_dic[words_lst[i]]:
            words_dic[words_lst[i]] += [words_lst[i + 1]]
    else:
        words_dic[words_lst[i]] = [words_lst[i + 1]]

# TODO: construct 5 random sentences
# Your code here
for i in range(5):
    word = random.choice(list(words_dic))
    string = word
    for j in range(random.randrange(15, 20)):
        if len(words_dic[word]) == 1:
            new_word = words_dic[word][0]
        else:
            new_word = words_dic[word][random.randrange(0, len(words_dic[word]) - 1)]
        string += " " + new_word
        word = new_word
    print(string[0].capitalize() + string[1:] + ".")
