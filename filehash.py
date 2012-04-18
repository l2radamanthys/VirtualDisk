#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Modulo para comprobar la suma MD5 de un archivo
"""

from hashlib import md5


def generate_sum(file_path):
    """
        calcula la suma MD5 de la cabercera de  un archivo
    """
    #file = open(file_path, 'rb')
    #header = file.read()
    header = open(file_path, 'rb').read()
    suma_md5 = md5(header).hexdigest()
    return suma_md5


def verify_sum(file_path, md5_sum):
    """
        Compara 2 suma MD5
    """
    file_md5_sum = generate_sum(file_path)
    return (file_md5_sum == md5_sum)


def equal_file_sum(file1_paht, file2_paht):
    """
        Compara si 2 archivos son iguales comparando su
        suma MD5
    """
    md5_sum1 = generate_sum(file1_path)
    md5_sum2 = generate_sum(file2_path)
    return (md5_sum1 == md5_sum2)


#test
if __name__ == '__main__':
    #prueba del calculador de hash
    import os
    
    root = "disk"
    f1 = "file1.sql"
    f2 = "file2.sql"
    
    s1 = generate_sum(os.path.join(root, f1))
    s2 = generate_sum(os.path.join(root, f2))
    
    print f1, "MD5 SUM ->", s1
    print f2, "MD5 SUM ->", s2
  
    print "son iguales?:", str(s1 == s2)

    
















