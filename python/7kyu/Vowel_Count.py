def get_count(sentence):
    vowel_count = 0
    for i in sentence:
        if i in "aeiou":
            vowel_count += 1
    return vowel_count
