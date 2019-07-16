from keras.datasets import reuters
import numpy as np


def load_article_data(num_words):
    (X_train, y_train), (X_test, y_test) = reuters.load_data(num_words=num_words, test_split=0.2)
    return (X_train, y_train), (X_test, y_test)


def indexing_words():
    word_index = reuters.get_word_index()
    index_to_word = {}
    for key, value in word_index.items():
        index_to_word[value] = key





