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

def random_word(file):
    words = decoding(load_words(file))
    return words

def return_words(file, words):
    save_word(file, encoding(words))
 

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