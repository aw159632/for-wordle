from nltk.corpus import words
from collections import Counter
import pandas as pd


def get_csrg_database(file_path):
    with open(file_path, 'r') as f:
        words_data = pd.Series(f.readlines())
        words_data = words_data.str.strip()

    return list(words_data)


def data_preprocessing(nltk_word_list, csrg_word_list):
    total_data = pd.Series(nltk_word_list + csrg_word_list)
    total_data = total_data.str.lower()
    # 去除重複值
    total_data = total_data.drop_duplicates()

    return list(total_data)


def write_files(output_path, words_data):
    with open(output_path, "w") as f:
        for word in words_data:
            f.write(word + "\n")


if __name__ == '__main__':
    nltk_word_list = words.words()
    csrg_word_list = get_csrg_database("csrg_words.txt")
    preprocessed_data = data_preprocessing(nltk_word_list, csrg_word_list)
    write_files("preprocessed_data.txt", preprocessed_data)
