#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os

from hash import *
from constantes import *


def gen_hash_path(path):
    """
    """
    data = []
    for root, dirs, files in os.walk(path):
        for file_name in files:
            #print dirs, file_name
            file_path = os.path.join(root, file_name)
            sum = generate_sum(file_path)
            #line = "%s;%s;%s;\n" %(root, file_name, sum)
            line = "%s;%s\n" %(file_path, sum)
            print line
            data.append(line)
    return data


def save_to_csv(data, file_name="hash.csv"):
    """
    """
    path = os.path.join(FOLDER_PATH, file_name)
    file = open(path, 'w')
    file.write("FILE PATH;SUMA MD5;\n")
    for line in data:
        file.write(line)
    file.close()





if __name__ == '__main__':
    data = gen_hash_path(FOLDER_PATH)#os.getcwd())
    save_to_csv(data)
    
