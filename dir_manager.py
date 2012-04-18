#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os

import filehash
from constantes import *



def get_files():
	data = []
	for path, folders, files in os.walk(FOLDER_PATH):
		for file_name in files:
			data.append((file_name, path, filehash.generate_sum(os.path.join(path, file_name))))
	return data	


#get_files()
