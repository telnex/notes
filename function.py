import sqlite3
import time
from config import *
import text
import json
import calendar
import logging
import datetime as dt


def check(id: int):
    """
    Проверка наличия пользователя ТГ в БД

    :param id: int
    :return: bool
    """
    connect = sqlite3.connect(BD)
    cur = connect.cursor()
    cur.execute('SELECT * FROM users where tg = ? ORDER BY id DESC limit 1;', [id, ])
    result = cur.fetchall()
    if len(result) == 0:
        cur.execute('INSERT INTO users (tg) VALUES (?);', [id, ])
        connect.commit()
    return True


def getLog():
    """ Получение основного лога бота """
    txt = open("./log/bot.log", "r", encoding='utf-8')
    file_log = txt.readlines()
    txt.close()
    num = len(file_log)
    log = ''
    if num > 15:
        i = 15
        while i > 0:
            log += str(file_log[num - i])
            i = i - 1
    else:
        txt = open("./log/bot.log", "r", encoding='utf-8')
        log = txt.read()
        txt.close()
    return log


def qCountUser():
    """ Кол-во пользователей бота"""
    connect = sqlite3.connect(BD)
    cur = connect.cursor()
    cur.execute('SELECT count(*) FROM users ;')
    result = cur.fetchone()
    return result[0]


def qCountNotes():
    """ Кол-во заметок в базе """
    connect = sqlite3.connect(BD)
    cur = connect.cursor()
    cur.execute('SELECT count(*) FROM notes;')
    result = cur.fetchone()
    return result[0]


def dateNowStr():
    """ Форматирование текущей даты в виде строки """
    day = dt.datetime.now().day
    year = dt.datetime.now().year
    month = dt.datetime.now().month
    date = str(day) + '.' + str(month) + '.' + str(year)
    return date

