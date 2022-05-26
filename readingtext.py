# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, 'r') as handler:
        return handler.read()
    #return "Hello World"


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    words = text.split()
    d = dict()
    for word in words:
        if word in d:
            d[word] = d[word]+1
        else:
            d[word] = 1
    print(d)

    #return {"as": 10, "would": 20}

