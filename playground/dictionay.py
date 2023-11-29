 
def create_word_dict(filename):
    word_dict = {}
    with open(filename, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                if word not in word_dict:
                    word_dict[word] = 1 
                else: 
                    word_dict[word] += 1 
    return word_dict

word_dict = create_word_dict("playground/dictionay.txt")

print(word_dict)
