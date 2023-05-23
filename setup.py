#!/usr/bin/env python

# $HeadURL: http://svn.berlios.de/svnroot/repos/mirageiv/branches/mirage-0.9.x/setup.py $
# $Id: setup.py 337 2011-02-13 22:40:05Z fredricj $

import os

from distutils.core import setup, Extension

def removeall(path):
	if not os.path.isdir(path):
		return

	files=os.listdir(path)

	for x in files:
		fullpath=os.path.join(path, x)
		if os.path.isfile(fullpath):
			f=os.remove
			rmgeneric(fullpath, f)
		elif os.path.isdir(fullpath):
			removeall(fullpath)
			f=os.rmdir
			rmgeneric(fullpath, f)

def rmgeneric(path, __func__):
	try:
		__func__(path)
	except OSError, (errno, strerror):
		pass

# Create mo files:
if not os.path.exists("mo/"):
	os.mkdir("mo/")
for lang in ('it', 'de', 'pl', 'es', 'fr', 'ru', 'hu', 'cs', 'pt_BR', 'zh_CN', 'nl', 'ua'):
	pofile = "po/" + lang + ".po"
	mofile = "mo/" + lang + "/microbox.mo"
	if not os.path.exists("mo/" + lang + "/"):
		os.mkdir("mo/" + lang + "/")
	print "generating", mofile
	os.system("msgfmt %s -o %s" % (pofile, mofile))

setup(name='MicroBox',
		version='1.0.0',
		description='An Scanner GUI',
		author='Zhenyu Geng',
		classifiers=[
			'Environment :: X11 Applications',
			'Intended Audience :: End Users/Desktop',
			'License :: GNU General Public License (GPL)',
			'Operating System :: Linux',
			'Programming Language :: Python',
			'Topic :: Multimedia :: Graphics :: Viewers'
			],
		py_modules = ['microbox'],
		ext_modules = [Extension(name='imgfuncs', sources=['imgfuncs.c']), 
		               Extension(name='xmouse', sources=['xmouse.c'], libraries=['X11'])],
		scripts = ['microbox'],
		data_files=[('share/microbox', ['README', 'COPYING', 'CHANGELOG', 'TODO', 'TRANSLATORS',
										'stock_crop.png', 'stock_flip-horizontally.png', 'stock_flip-vertically.png', 'stock_resize.png', 'stock_rotate-left.png',
										'stock_rotate-right.png', 'stock_shuffle.png', 'stock_leave-fullscreen.png', 'stock_fullscreen.png', 'mirage_blank.png']),
			('share/applications', ['microbox.desktop']),
			('share/pixmaps', ['mirage.png']),
			('share/locale/zh_CN/LC_MESSAGES', ['mo/zh_CN/microbox.mo'])],
		)

# Cleanup (remove /build, /mo, and *.pyc files:
print "Cleaning up..."
#try:
#	removeall("build/")
#	os.rmdir("build/")
#except:
#	pass
#try:
#	removeall("mo/")
#	os.rmdir("mo/")
#except:
#	pass
try:
	for f in os.listdir("."):
		if os.path.isfile(f):
			if os.path.splitext(os.path.basename(f))[1] == ".pyc":
				os.remove(f)
except:
	pass
