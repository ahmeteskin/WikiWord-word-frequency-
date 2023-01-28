import sqlite3
import ast
from typing import Dict
import json

from WikiWord.Qwe import functions
import re

class SqlDb():
    def __init__(self):
        #super(SqlDb, self).__init__()
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
        #o = dict(ope)
        op = ast.literal_eval(ope)
        #o = {"a":"a"}
        #k = json.loads(o)
        #a = json.loads(ope)
        #print(a)
        #print("**************************************************************************************************************************************************************************",ope,"***************")
        for i,v in op.items():
         #op = json.loads(line)
         #print(v)
         self.cur.execute('''INSERT OR IGNORE INTO WikiWord (Name, Percentage)
                 VALUES ( ?, ?)''', (i, v))
        self.sql.commit()


        #url = urllib.request.urlopen("https://www.imdb.com/chart/top/")  # .read().decode()
        #soup = BeautifulSoup(url, "html.parser")
        #tags = soup("td", class_='titleColumn')
        #l = []
        #tags2 = soup("td", class_="ratingColumn imdbRating")
        ##ta = functions.WikiWor()
        ##tags = ta.calculate()
        ##print(f"""
        ##************************************************
        ##{tags}
        ##************************************************""")
       ## #tags.count


        ### print(count)
       ## # print(l)
        ###for i,k in op:
        ###   print(i)
       ##     name = i.strip()
       ##     per = k
       ##     #per = re.findall("[0-9]+", per)
       ##     # print(date)
       ##     # for k in i:
       ##     #    k = k.lstrip()
       ##     #    #name = i[]
       ##     #    #date =
       ##     self.cur.execute('''INSERT OR IGNORE INTO wikiWords (Name, Percentage)
       ##             VALUES ( ?, ?)''', (name, per))
       ##     # cur.execute('''INSERT OR IGNORE INTO Film (Date)
       ##     #        VALUES ( ? )''', (date,))
##
       ## self.sql.commit()


