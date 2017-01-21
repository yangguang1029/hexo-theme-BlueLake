# -*- coding: UTF-8 -*- 
import os
import shutil

def main():
	print("start hexo clean....")
	os.system("hexo clean")
	print("start hexo g....")
	os.system("hexo g")

	for fname in os.listdir("./other"):
		spath = os.path.join(".", "other", fname)
		dpath = os.path.join(".", "public", fname)
		shutil.copy(spath, dpath)
	print("start hexo d....")
	os.system("hexo d")
	
if __name__ == '__main__':
	main()