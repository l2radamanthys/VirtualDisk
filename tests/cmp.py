#!/usr/bin/env python
# -*- coding: utf-8 -*-


import hashlib

def checksum(file):
	md5 = hashlib.md5()
	md5.update(open(file).read())
	return md5.hexdigest()


def main():
	print checksum("cmp.py")

if __name__ == '__main__':
	main()
