import os, re

regex = '_(.*)\.scss'
directory = '.'

for filename in os.listdir(directory):
	if filename.startswith('_'):
		name = re.search(regex, filename)
		name = name.group(1) + '.css'
		
		os.rename(filename, name)

		print 'Arquivo renomeado: [%s][%s]'%(filename, name)