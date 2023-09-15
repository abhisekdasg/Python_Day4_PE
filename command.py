# command.py file

import sys
from wordcount import count_words

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python command.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    word_count = count_words(filename)
    
    for word, count in word_count.items():
        print(f"*    {word} -------> {count}",' '* (61-len(word)),'*')
    
    print('*' * 80)