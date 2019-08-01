#!/usr/bin/env python
# coding: utf-8

import tempfile
import subprocess
import shutil
import os

class TnefMgr:
	def __init__(self,path):
		self.fpath=path
		self.tmpPath=None

	def close(self):
		if self.tmpPath == None:
			return

		for root, dirs, files in os.walk(self.tmpPath, topdown=False):
			for name in files:
				os.remove(os.path.join(root, name))
			for name in dirs:
				os.rmdir(os.path.join(root, name))
		os.rmdir(self.tmpPath)
		self.tmpPath = None

	def open(self):
		print "Abriendo"
		self.tmpPath = tempfile.mkdtemp()
		subprocess.call(["/usr/bin/tnef", "-f", self.fpath, "-C", self.tmpPath])

	def preview(self,file):
		os.system("xdg-open '%s/%s'" % (self.tmpPath,file))

	def getSize(self,file):
		return os.path.getsize("%s/%s" % (self.tmpPath,file) )

	def extract(self,file,to):
		shutil.copy( '%s/%s' % (self.tmpPath,file), to )

	def list(self):
		if self.tmpPath == None:
			return []
		return os.listdir(self.tmpPath)

