import db_Process
import MeCab
import re
from collections import Counter
from itertools import chain

subjects = db_Process.loadArticles()
vocab = Counter()

def spacing_Subjects():
    mecab = MeCab.Tagger('-Owakati')
    result = []
    for item in subjects:
        result.append(mecab.parse(item))
    return result

def tokenizing_Subject():
    subjects = spacing_Subjects()
    mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/ipadic')
    mecab.parse('')
    for i in subjects:
        parse = mecab.parse(i)
        lines = parse.split('\n')
        items = (re.split('[\t,]', line) for line in lines)
        find_Nouns(items)

    vocab_sorted = sorted(vocab.items(), key=lambda x: x[1], reverse=True)
    wordsToIndex(vocab_sorted)

def find_Nouns(items):
    for item in items:
        if (item[0] not in ('EOS', '', 't', 'ー', stop_words) and
                             item[1] == '名詞' and item[2] == '一般'):
            vocab[item[0]] = vocab[item[0]] + 1

def wordsToIndex(vocab_sorted):
    word_to_index = {}
    i = 0
    for (word, frequency) in vocab_sorted:
        if frequency > 1:  # 정제(Cleaning) 챕터에서 언급했듯이 빈도수가 적은 단어는 제외한다.
            i = i + 1
            word_to_index[word] = i
    print(word_to_index)

# def counting_Words(words):
#     counter = Counter(words)
#     for word, count in counter.most_common():
#         print(f"{word}: {count}")

path = "stop_words.txt"
stop_words = db_Process.create_stopwords(path)

tokenizing_Subject()

complete_kangi_range = range(0x4E00, 0x9FBF)
complete_jpn_range = range(0x3040, 0x31FF)
for i in chain(complete_jpn_range, complete_kangi_range):
    print(chr(i))
