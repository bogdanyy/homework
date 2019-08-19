#!/usr/bin/python3
import json
import sys
import sqlite3
import os
date_path = "/home/user/Документы/homework/HW/dict.db"



def create_db(date_path):
    if not os.path.isfile(date_path):
        with open(date_path,"wb") as file:
            pass
        return

def get_connect(date_path):
    connect = sqlite3.connect(date_path)
    return connect

def create_table(connect):
    sql_dict = """CREATE TABLE IF NOT EXISTS"dictionary"(
        "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        "word" TEXT NOT NULL,
        "lang_out" TEXT NOT NULL,
        "lang_in" TEXT NOT NULL,
        "translation" TEXT,
        "meaning"  TEXT
    );"""
    cursor = connect.cursor()
    cursor.execute(sql_dict)
    connection.commit()

def send_date(element, connect):
    #print()
    sql = f"""INSERT INTO "dictionary"(
      "id",
      "word",
      "lang_out",
      "lang_in",
      "translation",
      "meaning"
      )
      VALUES(
      "{element['word']}",
      "{element['lang_out']}",
      "{element['lang_in']}"
      "{element['translation']}"
      "{element['meaning']}"
      );"""
    cursor=connect.cursor()
    cursor.execute(sql)
    connection.commit()

if __name__ == "__main__":
    path = "/home/user/Документы/homework/HW/dict.db"
    create_db(date_path)
    connection = get_connect(date_path)
    create_table(connection)
    element =({'word':'вечер','lang_out':'ru','lang_in':'en','translation':'evening',
        'meaning':'вечеринка'})
    connect=get_connect(date_path)
    send_date(element,connect)
