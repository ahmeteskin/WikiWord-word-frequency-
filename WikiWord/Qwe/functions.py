from selenium import webdriver
from selenium.webdriver.common.by import By
from WikiWord.Qwe import values
from WikiWord.Qwe import sqldb
import string
import re


class WikiWor(webdriver.Chrome):
    def __init__(self, switch = True):
        super(WikiWor, self).__init__()
        self.sw = switch
        
    def onoff(self):
        return self.sw

    def opener(self):
        self.get(values.url)
        self.implicitly_wait(10)
        self.maximize_window()

    def enter(self):
        self.implicitly_wait(10)
        search = self.find_element(By.XPATH, "//*[@id=\"searchInput\"]")
        search.click()
        search.send_keys(values.inp)
        button = self.find_element(By.XPATH, "/html/body/div[5]/div/a[1]/div")
        button.click()
    def get_words(self):
        self.implicitly_wait(10)
        gett = self.find_elements(By.TAG_NAME, "p")
        self.gett = gett
        return self.gett

    def calculate(self):
        dic = dict()
        newdic = dict()
        count = 0
        for line in WikiWor.get_words(self):
            lin = line.text.lower()

            a = lin.split()
            for p in range(len(a)):
                    if "[" in a[p]:
                        q = a[p].split("[")
                        a.remove(a[p])
                        for o in range(len(q)):
                            if "]" not in q[o] or "[" not in q[o]:
                                a.append(q[o])

            for k in a:
                    dic[k] = dic.get(k, 0) + 1
            for e, p in dic.items():
                count += p
        for q, w in dic.items():
            newdic[q] = "{} %".format(float(w / count) * 100)

        t = open("tex.text", "w", encoding="utf-8")
        t.write(f"{newdic}")

    def db(self):
        y = sqldb.SqlDb()
        y.create_db()
        y.get_data()

