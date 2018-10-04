# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 23:14:45 2018
@AUTHOR PRAVEEN KUMAR

"""

import sqlite3
#iss code ko backend.py se save karna

def connect():
    conn = sqlite3.connect('student.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS data(id INTEGER PRIMARY KEY,name text,username text,email_id text,password text)")
    conn.commit()
    conn.close()


def insert(name,username, email_id, password):

    conn = sqlite3.connect('student.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO data VALUES(NULL,?,?,?,?)", (name,username, email_id, password))
    conn.commit()
    conn.close()
    k=("select * from data")
    return k[0]


def view():
    conn = sqlite3.connect('student.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM data")
    row = cur.fetchall()
    conn.close()
    return row


def search(name='',username='', email_id='', password=''):
    conn = sqlite3.connect('student.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM data WHERE name=? OR username=? OR email_id=? OR password=?", (name,username, email_id, password))

    rows = cur.fetchall()
    conn.close()
    return rows

def update(id,name,username, email_id, password):
    conn = sqlite3.connect('student.db')
    cur = conn.cursor()
    cur.execute("UPDATE  data SET  name=? OR username=? OR email_id=? OR password=? WHERE id=?", (name,username, email_id, password,id))
    conn.commit()
    conn.close()
def delete(id):
    conn = sqlite3.connect('student.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM data WHERE id=?",(id,))
    conn.commit()
    conn.close()

    




connect()
#insert("deepak","kumar","qasselephant","fucku")
#delete(1)
#update(1,'vikash','kumar','qasselephant','fucku')

print(search(name='armaan'))
#print(view())

