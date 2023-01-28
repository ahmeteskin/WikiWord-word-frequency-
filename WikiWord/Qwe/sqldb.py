import sqlite3
import ast
from typing import Dict
import json

from WikiWord.Qwe import functions
import re

class SqlDb():
    def __init__(self):
        pass


    def create_db(self):
        sql = sqlite3.connect("wikiWords.db")
        self.sql = sql
        cur = sql.cursor()

        cur.executescript("""
                DROP TABLE IF EXISTS WikiWord;
                CREATE TABLE IF NOT EXISTS WikiWord(ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, Name TEXT, Percentage FLOAT)""")
        self.cur = cur
    def get_data(self):

        opener = open("tex.text")
        ope = opener.read()
        op = ast.literal_eval(ope)
        for i,v in op.items():
         self.cur.execute('''INSERT OR IGNORE INTO WikiWord (Name, Percentage)
                 VALUES ( ?, ?)''', (i, v))
        self.sql.commit()
