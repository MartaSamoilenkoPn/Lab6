from typing import List
import copy
import random


def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',\
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    result_list = []
    for i in range(3):
        local_list = []
        for j in range(3):
            local_list.append(alphabet_list[random.randint(0, 25)])
        result_list.append(local_list)
    return result_list

def get_words(file_name: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    str_result = ""
    result_list = []
    with open(file_name, 'r') as file:
        str_result = file.read()
        words_list = str_result.split('\n')
        words_list.pop(0)
        words_list.pop(0)
        words_list.pop(0)
        for element in words_list:
            if len(element) > 3 and letters[4] in element:
                letters_copy = copy.deepcopy(letters)
                flag = True
                for letter in element.lower():
                    if letter in letters_copy:
                        letters_copy.remove(letter)
                    else:
                        flag = False
                        break
                if flag:
                    result_list.append(element.lower())
    return result_list


def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter 
    for Windows.
    Note: the user presses the enter key after entering each word.
    """
    list_input = []
    input_value = input()
    while input_value != '':
        list_input.append(input_value)
        input_value = input()
    return list_input


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    result_list = []
    for user_word in user_words:
        copy_letters = copy.deepcopy(letters)
        flag = True
        for letter in user_word:
            if letter not in copy_letters:
                flag = False
                break
        if flag:
            if user_word not in words_from_dict:
                result_list.append(user_word)
    return result_list

def results():
    with open('result.txt', 'w') as file:
        grid = generate_grid()
        letters = []
        for row in grid:
            for letter in row:
                print(letter, end=' ')
                letters.append(letter.lower())
            print()
        dict_words = get_words('words.txt', letters)
        user_words = get_user_words()
        non_dict_words = get_pure_user_words(user_words, letters, dict_words)
        right_words_number = len(user_words) - len(non_dict_words)
        non_input_words = []
        for word in dict_words:
            if word not in user_words:
                non_input_words.append(word)

        file.write(str(right_words_number)+'\n')
        file.write(str(non_input_words)+'\n')
        file.write(str(non_dict_words))

if __name__ == "__main__":
    results()
