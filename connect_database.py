import sqlite3
import logging
# logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s',datefmt='%H:%M:%S', level=logging.DEBUG)


# Create database
# columns:
# id | name | fr_name | en_name | part_of_speech | synonym | coupling | image |

database = 'dictionary.db'

class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.create_general_language('pl_words')

    def create_general_language(self, name_table):
        self.cur.execute(f"""CREATE TABLE IF NOT EXISTS '{name_table}' (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            part_of_speech TEXT
            )""")    

    def fetch(self, name_table):
        self.cur.execute(f"SELECT * FROM '{name_table}'")
        rows = self.cur.fetchall()
        return rows

    def take_word_row(self, name_table, word):
        self.cur.execute(f"SELECT * FROM '{name_table}' WHERE name='{word}'")
        word = self.cur.fetchone()
        return word
    
    def take_id_row(self, name_table, id):
        self.cur.execute(f"SELECT * FROM '{name_table}' WHERE id='{id}'")
        word = self.cur.fetchone()
        return word

    def select_names_of_words(self, name_table):
        self.cur.execute(f"SELECT name FROM '{name_table}'")
        rows = self.cur.fetchall()
        words = []
        for word in rows:
            words.append(word[0])
        return words

    def show_all_tables(self):
        self.cur.execute("""SELECT name FROM sqlite_schema 
                WHERE type IN ('table','view') 
                AND name NOT LIKE 'sqlite_%'
                ORDER BY 1;""")

        tables = self.cur.fetchall()
        return tables

    def insert(self, name_table, name, part_of_speech):
        self.cur.execute(f"INSERT INTO '{name_table}' VALUES (NULL, ?, ?)", 
                            (name, part_of_speech))
        self.conn.commit()
        logging.info(f"Insert name: {name}, part_of_speech: {part_of_speech}")

    def remove(self, name_table, id):
        row = self.take_id_row(name_table, id)
        self.cur.execute(f"DELETE FROM '{name_table}' WHERE id=?", (id,))
        self.conn.commit()
        logging.info(f"Remove row: {row}")

    def update(self, name_table, id, name, part_of_speech):
        self.cur.execute(f"UPDATE '{name_table}' SET name = ?, part_of_speech = ? WHERE id = ?", (name, part_of_speech, id))
        self.conn.commit()
        logging.info(f"Update name: {name}, part_of_speech: {part_of_speech}")

    def __del__(self):
        self.conn.close()


# Class for create new table in the database
class AddNewLanguage(Database):

    def __init__(self, db, name_table):
        super().__init__(db)

        self.name_table = name_table
        self.add_table()

    def add_table(self):
        self.cur.execute(f"""CREATE TABLE IF NOT EXISTS '{self.name_table}' (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            word_pl INTEGER NOT NULL,
            part_of_speech TEXT,
            synonym TEXT,
            coupling TEXT,
            image BLOB,
            FOREIGN KEY (word_pl) REFERENCES pl_words(id)
            )""")

    def take_pl_id(self, pl_id):
        self.cur.execute(f"SELECT * FROM '{self.name_table}' WHERE word_pl={pl_id}")
        rows = self.cur.fetchall()
        return rows

    def find_words(self, word):
        self.cur.execute(f"SELECT * FROM '{self.name_table}' WHERE name='{word}'")
        rows = self.cur.fetchall()
        return rows

    def insert(self, name, word_pl, part_of_speech, synonym, coupling, image):
        self.cur.execute(f"INSERT INTO '{self.name_table}' VALUES (NULL, ?, ?, ?, ?, ?, ?)", 
                            (name, word_pl, part_of_speech, synonym, coupling, image))
        self.conn.commit()

    def update(self, id, name, world_pl, part_of_speech, synonym, coupling, image):
        self.cur.execute(f"UPDATE '{self.name_table}' SET name = ?, world_pl = ?, part_of_speech = ?, synonym = ? \
            coupling = ?, image = ? WHERE id = ?", (name, world_pl, part_of_speech, synonym, coupling, image, id)) 
        self.conn.commit()





db = Database(database)
en = AddNewLanguage(database, "en_words")
fr = AddNewLanguage(database, "fr_words")

