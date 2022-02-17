# import nltk
# nltk.download()

from nltk.corpus import words
from collections import Counter
import pandas as pd


def get_database_from_txt(file_path):
    with open(file_path, 'r') as f:
        words_data = pd.Series(f.readlines())
        words_data = words_data.str.strip()

    return list(words_data)


def get_correct_word(total_words):
    # 綠色
    dic_correct_letter = {"2": "a", "0": "s", "4": "e", "1": "h"}
    # 黃色 + 錯誤的位置資訊
    dic_position_error_letter = [("0", "a"), ("1", "a"), ("3", "e")]
    # 黃色
    wrong_position_letters = ["a", "e", "s"]
    # 灰色
    wrong_totaly_letters = ["u", "d", "i", "o", "b", "l", "r", "y", "t", "p", "c", "v"]
    # 是否要重複字母
    duplicate = True

    statistic_letter = {}
    for word in total_words:
        word = word.lower()
        # 只保留五個字的單字
        if len(word) != 5:
            continue

        # 去除沒有出現的單字
        wrong_letter_single = False
        for wrong_letter in wrong_totaly_letters:
            if wrong_letter in word:
                wrong_letter_single = True
                break
        if wrong_letter_single:
            continue

        # 去除沒有包含某字元的單字
        wrong_letter_single = False
        for wrong_position_letter in wrong_position_letters:
            if wrong_position_letter not in word:
                wrong_letter_single = True
                break
        if wrong_letter_single:
            continue

        # 去除某字元沒有正確位置的單字 - 根據正確位置的字母
        wrong_letter_single = False
        if len(dic_correct_letter) != 0:
            for position in dic_correct_letter.keys():
                if word[int(position)] != dic_correct_letter[position]:
                    wrong_letter_single = True
                    break
            if wrong_letter_single:
                continue

        # 去除某字元沒有正確位置的單字 - 根據錯誤位置的字母
        wrong_letter_single = False
        if len(dic_position_error_letter) != 0:
            for position_value in dic_position_error_letter:
                if word[int(position_value[0])] == position_value[1]:
                    wrong_letter_single = True
                    break
            if wrong_letter_single:
                continue

        # 去除有重複字元的單字
        wrong_letter_single = False
        if not duplicate:
            counter = Counter(word)
            for value in counter.values():
                if value >= 2:
                    wrong_letter_single = True
                    break
            if wrong_letter_single:
                continue

        print(word)

        # 方便使用者猜下一輪的單字 -> 統計有可能的英文單字中，其字母的出現個數
        for letter in word:
            if letter not in statistic_letter.keys():
                statistic_letter[letter] = 1
            else:
                statistic_letter[letter] += 1
    # print(statistic_letter)
    # for key in sorted(statistic_letter.keys()):
    #     print("{key}: {value}".format(key=key, value=statistic_letter[key]))
    print("\n---- statistic letter ----")
    for key, value in sorted(statistic_letter.items(), key=lambda x: x[1], reverse=True):
        print("{key}: {value}".format(key=key, value=value))


if __name__ == '__main__':
    # word_list = words.words()
    word_list = get_database_from_txt("preprocessed_data.txt")
    get_correct_word(word_list)
