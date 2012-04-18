#!/usr/bin/env python
# -*- coding: utf-8 -*-


#import sqlite3
import ftplib

import csv
from constantes import *


def compare_files():
    local_reader = csv.reader(open("hash.csv", "r"), delimiter=";")
    server_reader = csv.reader(open("hash.csv", "r"), delimiter=";")
    dict = {}
    for row in local_reader:
        dict[row[0]] = row[1]
    print dict

def main():
    conecion = ftplib.FTP(SERVER, USER, PSWR)
    conecion.cwd(ROOT_FOLDER)


if __name__ == "__main__":
    compare_files()


