# Iportando modulos
import os
import time
import shutil
import urllib.request
from tqdm import tqdm

versao = urllib.request.urlopen('Insira aqui o link').read().decode('utf8').splitlines()[0] # Link do RAW do arquivo contendo a versao
changelogs = urllib.request.urlopen('Insira aqui o link').read().decode('utf8') # Link do RAW do arquivo contendo o changlog
link = 'Insira aqui o link' # Link do download no GitHub
path = 'arquivo.zip' # Nome que deseja para o arquivo

# Checando nova versão
if versao == '1.0.0': # Coloque aqui a versão
	print('Nenhuma nova versão encontrada.')
	input()
else:
	if os.path.exists('Atualizado para a versão ' + versao):
		print('A atualização foi instalada.')
		input()
	else:
		print('Atualização disponível.')
		print('\n=-==-==-==-==-==-==-=')
		print('Changelogs:\n' + changelogs)
		print('=-==-==-==-==-==-==-=\n')
		print('Atualizar agora? s/n\n')
		if input().lower() == 's'.lower():
			print('\nBaixando atualização...')
			urllib.request.urlretrieve(link, path)
			print('Descompactando arquivo...')
			shutil.unpack_archive(path, 'Atualizado para a versão ' + versao)
			os.remove(path)
			for i in tqdm(range(100)):
    				time.sleep(0.1)
			print('\nA atualização foi instalada, aperte qualquer tecla para sair.')
			input()
