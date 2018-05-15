
# counts chosen word in txt file
# python2 wordcounter.py file.txt word

import sys

def count_word(stream, word):
    count = 0
    words = []

    for line in stream:
        words.extend(line.split())
    
    for w in words:
        if w.lower() == word:
            count += 1
    return count




if __name__ == '__main__':

    file = sys.argv[1]
    word = sys.argv[2]

    with open(file, 'r') as input:
        print(count_word(input, word))

    
