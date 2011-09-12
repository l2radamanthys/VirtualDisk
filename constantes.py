#!/usr/bin/env python
# -*- coding: utf-8 -*-


#DATOS FTP
SERVER = "ftp.fileserve.com" #servidor ftp
USER = "LRadamanthys" #usuario
PSWR = "2b741a2c" #pswr
ROOT_FOLDER = "/public_html" #carpeta raiz


#DATOS LOCALES
FOLDER_PATH = "disk" #carpeta q funcionara como disco virtual
DB_FOLDER = ".virtualdisk"
DB_NAME = "database.db"



SQL_TABLE = """
CREATE TABLE Files (
    name VARCHAR(250),
    path VARCHAR(250),
    md5 VARCHAR(30)
);
"""

