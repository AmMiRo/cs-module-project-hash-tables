import re

def word_count(s):
    # Your code here
    cache = {}
    if s == "":
        return cache
    string = s.lower()
    forbidden_char = ["\"", "\\", ":", ";", ",", ".", "-", "+", "=", "/", "|", "[", "]", "{", "}", "(", ")",  "*", "^", "&"]
    alt_white_space = ["\n", "\r", "\t"]
    for char in forbidden_char:
        string = string.replace(char, "")
    for space in alt_white_space:
        string = string.replace(space, " ")
    words = string.split(" ")
    for word in words:
        if word != "":
            if word in cache:
                cache[word] += 1
            else:
                cache[word] = 1
    print(cache)
    return cache



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))