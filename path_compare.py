#!/usr/bin/env python
# -*- coding: utf-8 -*-


from hash import *
import os

#path, file_name, md5


def gen_hash_path(path):
    """
    """
    for root, dirs, files in os.walk(path):
        for file_name in files:
            #print dirs, file_name
            file_path = os.path.join(root, file_name)
            print file_path
            



if __name__ == '__main__':
    gen_hash_path(os.getcwd())
