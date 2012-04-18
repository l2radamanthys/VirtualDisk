#!/usr/bin/env python
# -*- coding: utf-8 -*-


#DATOS FTP
SERVER = "server17.000webhost.com" #servidor ftp
USER = "a4050719" #usuario
PSWR = "inmortal" #pswr
ROOT_FOLDER = "/public_html" #carpeta raiz


#DATOS LOCALES
FOLDER_PATH = "D:\Proyectos\VirtualDisk\disk" #carpeta q funcionara como disco virtual
DB_FOLDER = ".virtualdisk"
DB_NAME = "database.db"



SQL_TABLE = """
CREATE TABLE Files (
    name VARCHAR(250),
    path VARCHAR(250),
    md5 VARCHAR(30)
);
"""

