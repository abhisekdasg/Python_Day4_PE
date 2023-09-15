# wordcount.py file

def count_words(filename):
    word_count = {}
    
    with open(filename, "r") as file:
        text = file.read()
        words = text.split()
       	
  
        for word in words:
            # Remove punctuation and convert to lowercase for accurate counting
            word = word.strip(".,!?").lower()
            
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    print()
    print('*' * 80)
    print('* Total no of words present in this file is: ',len(words),' '*(33-len(word)),'*')
    print('*' * 80)


    
    return word_count
