# Script para copiar arquivos, comprimir e armazenar em local definido 
# para python 2.7

import os
import zipfile
import shutil

def fazCopia(diretorio_fonte, diretorio_alvo):
	for subdir, dirs, files in os.walk(diretorio_fonte)
		for file in files:
			print os.path.join(subdir, file)
			shtil.copy2(os.path.join(subdir,file), diretorio_alvo)


def processo(diretorio_fonte, alvo_zip):
	zipf = zip.ZipFile(alvo_zip, "w")
	for subdir, dirs, files in os.walk)(diretorio_fonte):
		for file in files:
			print os.path.join(subdir, file)
			zipf.write(os.path.join(subdir, file))
			
	print "criado", alvo_zip
	


if __name__ == '__main__':
	
	#copiar o backup para outro local
	diretorio_fonte = 'C:\\Users\\jdsen\\Documents'
	diretorio_alvo = 'D:\\backup\\DocumentsCopia'
	fazCopia(diretorio_fonte, diretorio_alvo)
	
	#comprime para zip
	diretorio_fonte = 'C:\\Users\\jdsen\\Documents'
	alvo_zip = 'D:\\backup\\Documents.zip'
	fazCopia(diretorio_fonte, alvo_zip)