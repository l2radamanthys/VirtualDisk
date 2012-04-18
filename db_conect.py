#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sqlite3

from constantes import *
import dir_manager as dm





class DBFiles:
	def __init__(self):
		"""
			Establece la connecion con la BD, y crea un apuntador para poder realizar consultas
		"""
		self.conn = sqlite3.connect(os.path.join(FOLDER_PATH, DB_NAME))
		self.cursor = self.conn.cursor()
		
		
	def update(self):
		"""
		"""
		for data in dm.get_files():
			query = "REPLACE INTO Local_Files (file_path, md5) VALUES (?,?)"
			#print data
			print data[0], data[2]
			self.cursor.execute(query, (data[0], data[2]))
		self.conn.commit()	
		
	
	
	
		
	
	

if __name__ == "__main__":
	f = DBFiles()
	f.update()
