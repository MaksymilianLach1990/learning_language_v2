# Load list of words
# Take 10 words
# Save list of words
# Encoding and decoding words


# !! Option save == ON !! kopia w image

import logging
import random
from connect_database import db
# logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s',datefmt='%H:%M:%S', level=logging.DEBUG)


# plik = "words_pl.txt"
brak = "Brak"

def load_words(file):
    with open(file, 'rb') as f:
        text = f.readlines()
        logging.debug(f"Number of load lines: {len(text)}")
        return text

def save_word(plik, words):
    with open(plik, 'wb') as f:
        logging.debug(f"Number of saveing words: {len(words)}")
        for word in words:
            f.write(word)

def decoding(words_list):
    words = []
    for word in words_list:
        word = word.decode('utf-8').strip()
        words.append(word)
    logging.debug(f"Number of decoding words: {len(words)}")
    return words

def encoding(words_list):
    words = []
    for word in words_list:
        word = word + '\n'
        word = word.encode('utf-8')
        words.append(word)
    logging.debug(f"Number of ancoding words: {len(words)}")
    return words

def take_word_and_update_list(plik):
    list_of_words = decoding(load_words(plik))
    table_words = db.select_names_of_words('pl_words')
    logging.debug(f"Number list_of_words: {len(list_of_words)} / table_words: {len(table_words)}")
    word = random.choice(list_of_words)
    list_of_words.remove(word)
    logging.debug(f"Random word: {word}")
    return word
 

"""
włańcza się
-pobiera i wyświetla pierwsze słowo
    wypełnianie inputów
    naciśnięcie next Słowo
    pobiera dane z inputów
    zapisuje dane w słowniku
    czyści pola inputów
    losuje nowe słowo
    wyświetla nowe słowo
- 
"""