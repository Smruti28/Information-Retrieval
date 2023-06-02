import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from itertools import chain
from collections import Counter


def get_logical_view():
    stop_words = list(stopwords.words('english'))
    stop_words = stop_words+['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', ';', '/', '.',
                             ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~', ',', '''"''', "'", "'''", 'e.g.',
                             'ex.', 'etc.', 'etc', 'could', 'would', 'should', 'must']
    tokenized_words = []
    logical_view = []
    for i in range(1, 11):
        file1 = open(f"document{i}.txt", 'r', encoding="utf8")
        for word in file1.readlines():
            tokenized_words.append(word_tokenize(word.strip('\n')))
        tokenized_words = list(chain(*tokenized_words))
        tokenized_words = [i.lower() for i in tokenized_words]
        processed_text = []
        for word1 in tokenized_words:
            if word1 not in stop_words and word1.isnumeric() == False and word1.isdecimal() == False and word1.isalpha() and len(word1) >= 3:
                processed_text.append(word1)
        logical_view.append(processed_text)
    # print(Counter((chain(*logical_view))))
    # logical_view = list(set(chain(*logical_view)))
    cnt_temp = Counter(chain(*logical_view))
    logical_view = [i for i, j in cnt_temp.items()]
    return logical_view


res = get_logical_view()
# print(res)
print("The logical view of document is:\n")
for i in range(len(res)):
    print(res[i], end=",")
