
#Script para backup, python versão 3.x

import shutil
import os

fonte = r"C:\Users\Public'"
destino = r"D:\backup"

arquivos = os.listdir(fonte)
aquivos

arquivos2 = os.listdir(destino)
arquivos2

os.chdir(fonte)

for arquivo in arquivos:
	with open(arquivo) as arq:
		print(arquivo,arq.read())

for arquivo in arquivos:
	if os.path.isfile(arquivo):
		shutil.copy(arquivo, destino)
	
		'''
		#Codigo para mover os arquivos e sobrescrever
		print(destino)
		destino_total = os.path.join(destino, arquivo)
		print(destino_total)
		shutil.move(file, destino_total)
		'''