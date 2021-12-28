# -*- coding: utf-8 -*-
import logging
from connect_database import db, en, fr
from list_of_words import take_word_and_update_list
from PyQt5.QtGui import QTextDocument
from PyQt5 import QtCore, QtGui, QtWidgets
# logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s',datefmt='%H:%M:%S', level=logging.DEBUG)
logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s',datefmt='%H:%M:%S', level=logging.INFO)
# logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s',datefmt='%H:%M:%S', level=logging.WARNING)
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")

logging.debug("Debug dla szukania błędów")
logging.info("Info dla informacji")
logging.warning("Dla przewidzianych błędów")

class Ui_MainWindow(object):
    
    # Take 10 words from file
    def prepare_words():
        quest = {}
        for word in range(10, 0, -1):
            quest[word] = take_word_and_update_list('words_pl.txt')
            logging.debug(f"{word} : {quest[word]}")
        return quest
    
    quest = prepare_words()
    logging.info(quest)

    words = {}

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(380, 620)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.exit_button = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.exit_app(self.rid_html(self.word.text())))
        self.exit_button.setGeometry(QtCore.QRect(30, 470, 320, 100))
        self.exit_button.setObjectName("exit_button")
        self.but_previous_word = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.previous_word(self.word.text(), self.words_num.text()))
        self.but_previous_word.setGeometry(QtCore.QRect(20, 400, 160, 60))
        self.but_previous_word.setObjectName("but_previous_word")
        self.but_next_word = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.next_word(self.word.text(), self.words_num.text()))
        self.but_next_word.setGeometry(QtCore.QRect(200, 400, 160, 60))
        self.but_next_word.setObjectName("but_next_word")
        self.lab_num_word = QtWidgets.QLabel(self.centralwidget)
        self.lab_num_word.setGeometry(QtCore.QRect(20, 0, 200, 30))
        self.lab_num_word.setObjectName("lab_num_word")
        self.words_num = QtWidgets.QLabel(self.centralwidget)
        self.words_num.setGeometry(QtCore.QRect(260, 0, 50, 30))
        self.words_num.setObjectName("words_num")
        self.lab_describ_word = QtWidgets.QLabel(self.centralwidget)
        self.lab_describ_word.setGeometry(QtCore.QRect(20, 40, 160, 30))
        self.lab_describ_word.setObjectName("lab_describ_word")
        self.word = QtWidgets.QLabel(self.centralwidget)
        self.word.setGeometry(QtCore.QRect(200, 40, 160, 30))
        self.word.setObjectName("word")
        self.lab_general_form = QtWidgets.QLabel(self.centralwidget)
        self.lab_general_form.setGeometry(QtCore.QRect(20, 80, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lab_general_form.setFont(font)
        self.lab_general_form.setObjectName("lab_general_form")
        self.input_general_form = QtWidgets.QTextEdit(self.centralwidget)
        self.input_general_form.setGeometry(QtCore.QRect(200, 80, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.input_general_form.setFont(font)
        self.input_general_form.setObjectName("input_general_form")
        self.lab_tranlate = QtWidgets.QLabel(self.centralwidget)
        self.lab_tranlate.setGeometry(QtCore.QRect(20, 120, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lab_tranlate.setFont(font)
        self.lab_tranlate.setObjectName("lab_tranlate")
        self.input_translate = QtWidgets.QTextEdit(self.centralwidget)
        self.input_translate.setGeometry(QtCore.QRect(200, 120, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.input_translate.setFont(font)
        self.input_translate.setObjectName("input_translate")
        self.lab_synonym = QtWidgets.QLabel(self.centralwidget)
        self.lab_synonym.setGeometry(QtCore.QRect(20, 160, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lab_synonym.setFont(font)
        self.lab_synonym.setObjectName("lab_synonym")
        self.input_synonym = QtWidgets.QTextEdit(self.centralwidget)
        self.input_synonym.setGeometry(QtCore.QRect(200, 160, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.input_synonym.setFont(font)
        self.input_synonym.setObjectName("input_synonym")
        self.lab_association = QtWidgets.QLabel(self.centralwidget)
        self.lab_association.setGeometry(QtCore.QRect(20, 200, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lab_association.setFont(font)
        self.lab_association.setObjectName("lab_association")
        self.input_assiociation = QtWidgets.QTextEdit(self.centralwidget)
        self.input_assiociation.setGeometry(QtCore.QRect(200, 200, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.input_assiociation.setFont(font)
        self.input_assiociation.setObjectName("input_assiociation")
        self.lab_part_of_speech = QtWidgets.QLabel(self.centralwidget)
        self.lab_part_of_speech.setGeometry(QtCore.QRect(20, 250, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lab_part_of_speech.setFont(font)
        self.lab_part_of_speech.setObjectName("lab_part_of_speech")
        self.input_part_of_speech = QtWidgets.QComboBox(self.centralwidget)
        self.input_part_of_speech.setGeometry(QtCore.QRect(200, 250, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.input_part_of_speech.setFont(font)
        self.input_part_of_speech.setObjectName("input_part_of_speech")
        self.but_a_1 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.add_akcent('â'))
        self.but_a_1.setGeometry(QtCore.QRect(50, 300, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.but_a_1.setFont(font)
        self.but_a_1.setObjectName("but_a_1")
        self.but_c_1 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.add_akcent('ç'))
        self.but_c_1.setGeometry(QtCore.QRect(50, 350, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.but_c_1.setFont(font)
        self.but_c_1.setObjectName("but_c_1")
        self.but_a_2 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.add_akcent('à'))
        self.but_a_2.setGeometry(QtCore.QRect(110, 300, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.but_a_2.setFont(font)
        self.but_a_2.setObjectName("but_a_2")
        self.but_i_1 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.add_akcent('î'))
        self.but_i_1.setGeometry(QtCore.QRect(110, 350, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.but_i_1.setFont(font)
        self.but_i_1.setObjectName("but_i_1")
        self.but_e_1 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.add_akcent('é'))
        self.but_e_1.setGeometry(QtCore.QRect(170, 300, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.but_e_1.setFont(font)
        self.but_e_1.setObjectName("but_e_1")
        self.but_o_1 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.add_akcent('ô'))
        self.but_o_1.setGeometry(QtCore.QRect(170, 350, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.but_o_1.setFont(font)
        self.but_o_1.setObjectName("but_o_1")
        self.but_e_2 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.add_akcent('è'))
        self.but_e_2.setGeometry(QtCore.QRect(230, 300, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.but_e_2.setFont(font)
        self.but_e_2.setObjectName("but_e_2")
        self.but_e_3 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.add_akcent('ê'))
        self.but_e_3.setGeometry(QtCore.QRect(290, 300, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.but_e_3.setFont(font)
        self.but_e_3.setObjectName("but_e_3")
        self.but_u_1 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.add_akcent('û'))
        self.but_u_1.setGeometry(QtCore.QRect(230, 350, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.but_u_1.setFont(font)
        self.but_u_1.setObjectName("but_u_1")
        self.but_u_2 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.add_akcent('ù'))
        self.but_u_2.setGeometry(QtCore.QRect(290, 350, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.but_u_2.setFont(font)
        self.but_u_2.setObjectName("but_u_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 380, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpisz_10_s_w = QtWidgets.QAction(MainWindow)
        self.actionOpisz_10_s_w.setObjectName("actionOpisz_10_s_w")
        self.actionDodaj_w_asne_s_owo = QtWidgets.QAction(MainWindow)
        self.actionDodaj_w_asne_s_owo.setObjectName("actionDodaj_w_asne_s_owo")
        self.actionZnajd_s_owo = QtWidgets.QAction(MainWindow)
        self.actionZnajd_s_owo.setObjectName("actionZnajd_s_owo")
        self.menuMenu.addAction(self.actionOpisz_10_s_w)
        self.menuMenu.addAction(self.actionDodaj_w_asne_s_owo)
        self.menuMenu.addAction(self.actionZnajd_s_owo)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.exit_button.setText(_translate("MainWindow", "Zapisz słowa"))
        self.but_previous_word.setText(_translate("MainWindow", "Porzednie słowo"))
        self.but_next_word.setText(_translate("MainWindow", "Następne słowo"))
        self.lab_num_word.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Liczba słów do opisania:</span></p></body></html>"))
        self.words_num.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">10</span></p></body></html>"))
        self.lab_describ_word.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Opisz słowo:</span></p></body></html>"))
        self.word.setText(_translate("MainWindow", f"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">{self.quest[10]}</span></p></body></html>"))
        self.lab_general_form.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Forma podstawowa</span></p></body></html>"))
        self.lab_tranlate.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Tłumaczenie</span></p></body></html>"))
        self.lab_synonym.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Podaj synonim</p></body></html>"))
        self.lab_association.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Podaj skojarzenie</p></body></html>"))
        self.lab_part_of_speech.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Wybierz część mowy</p></body></html>"))
        part_of_speech_pl = ['','null', 'rzeczownik', 'czasownik', 'przymiotnik', 'liczebnik', 'zaimek', 'przysłówek', 'przyimek', 'spójnik', 'wykrzyknik', 'partykuła']
        for part in part_of_speech_pl:
            self.input_part_of_speech.addItem(part)
        self.but_a_1.setText(_translate("MainWindow", "â"))
        self.but_c_1.setText(_translate("MainWindow", "ç"))
        self.but_a_2.setText(_translate("MainWindow", "à"))
        self.but_i_1.setText(_translate("MainWindow", "î"))
        self.but_e_1.setText(_translate("MainWindow", "é"))
        self.but_o_1.setText(_translate("MainWindow", "ô"))
        self.but_e_2.setText(_translate("MainWindow", "è"))
        self.but_e_3.setText(_translate("MainWindow", "ê"))
        self.but_u_1.setText(_translate("MainWindow", "û"))
        self.but_u_2.setText(_translate("MainWindow", "ù"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionOpisz_10_s_w.setText(_translate("MainWindow", "Opisz 10 słów"))
        self.actionDodaj_w_asne_s_owo.setText(_translate("MainWindow", "Dodaj własne słowo"))
        self.actionZnajd_s_owo.setText(_translate("MainWindow", "Znajdź słowo"))

    

    # Button for franch accents
    def add_akcent(self, akcent):
        # Dorobić śledzenie kursora, tak aby nie znikał przy naciśnięciu guzika
        self.input_translate.setText(f'{self.input_translate.toPlainText()}{akcent}')

    # Write the data in the dictionary for this section
    def save_word(self, word):
        self.words[word] = {'word_pl': self.rid_html(self.input_general_form.toPlainText()),
                            'word_fr': self.rid_html(self.input_translate.toPlainText()),
                            'synonym': self.rid_html(self.input_synonym.toPlainText()),
                            'assiociation': self.rid_html(self.input_assiociation.toPlainText()), 
                            'part of speech': self.rid_html(self.input_part_of_speech.currentText())
                            }
        logging.debug(f'Save word: {word}')

    # Take only text from html code
    def rid_html(self, phrase):
        doc = QtGui.QTextDocument()
        doc.setHtml(phrase)
        phrase = doc.toPlainText()
        return phrase

    # Clean all input fields
    def clean_input_fields(self):
        logging.debug('Clean input fields')
        self.input_general_form.setText('')
        self.input_translate.setText('')
        self.input_synonym.setText('')
        self.input_assiociation.setText('')
        self.input_part_of_speech.setCurrentIndex(0)

    # Go to the next word
    def next_word(self, word, count):
        word = self.rid_html(word)
        count = self.rid_html(count)
        self.save_word(word)
        logging.debug(f"Words : {self.words.keys()}")
        if int(count) == 1:
            logging.debug("All words are described")
            logging.debug("Dorobić okienko z wiadomością")
            return
        self.clean_input_fields()
        count = int(count) - 1
        next_word = self.quest[int(count)]
        self.fill_input_fields(next_word)
        logging.debug(f"Next word : {next_word} | {count}")    
        _translate = QtCore.QCoreApplication.translate
        self.word.setText(_translate("MainWindow", f"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">{next_word}</span></p></body></html>"))
        self.words_num.setText(_translate("MainWindow", f"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">{str(count)}</span></p></body></html>"))

    # Fill in the fields with the information from the dictionary
    def fill_input_fields(self, word):
        try:
            data = self.words[word]
            logging.debug('Fields filled')
            self.input_general_form.setText(data['word_pl'])
            self.input_translate.setText(data['word_fr'])
            self.input_synonym.setText(data['synonym'])
            self.input_assiociation.setText(data['assiociation'])
            self.input_part_of_speech.setCurrentText(data['part of speech'])
        except KeyError as e:
            logging.debug(f'A word: {word}; does not exist yet')
            return

    # Go to the previous word
    def previous_word(self, word, count):
        logging.debug('Zrów tak aby pola się automatycznie uzupełniały')
        word = self.rid_html(word)
        count = self.rid_html(count)
        self.save_word(word)
        logging.debug(f"Present_word : {word} | {count}")

        if int(count) == 10:
            logging.debug(f"This is first word")
            logging.debug("Dorobić okienko z wiadomością")
            return
        count = int(count) + 1
        previous_word = self.quest[int(count)]
        self.fill_input_fields(previous_word)
        logging.debug(f"Prvious_word : {previous_word} | {count}")
        _translate = QtCore.QCoreApplication.translate
        self.word.setText(_translate("MainWindow", f"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">{previous_word}</span></p></body></html>"))
        self.words_num.setText(_translate("MainWindow", f"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">{str(count)}</span></p></body></html>"))
        
    # Insert data into database at the end
    def insert_data(self):
        logging.debug("Inserting data")

    # Exit with a button
    def exit_app(self, word):
        self.save_word(word)
        logging.debug("Exit program")
        logging.debug("Upewnij się że dane się zapisują :)")
        self.insert_data()
        exit()

# Run app
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

