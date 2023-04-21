import pywhatkit as kt
import os

pasta = './images/'
dest = './converted/'

if not os.path.exists(dest):
    os.mkdir(dest)

if not os.path.exists(pasta):
    os.mkdir(pasta)

print(f'\t\t=====ATENÇÃO!=====\n\tCaso seja sua primeira vez executando o código,\n\tprovavelmente ele só irá criar as pastas iniciais\n\tExecute novamente após isso com os arquivos na pasta \"images\" \n\tpara o código funcionar corrretamente\n')

for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        output = ' '
        print(f'Arquivo encontrado: \t{os.path.join(diretorio, arquivo)}')
        try:
            txtArquivo = arquivo + ".txt"
            kt.image_to_ascii_art(pasta + arquivo, dest + txtArquivo)
            output = (f'Arquivo Convertido: \t{os.path.join(diretorio, arquivo)}')
            print(f'Arquivo Convertido: \t{os.path.join(diretorio, arquivo)}')

        except:
            output = print(f'Erro ao converter: \t{os.path.join(diretorio, arquivo)}')
            print(f'Erro ao converter: \t{os.path.join(diretorio, arquivo)}')
        
        print(f'='*(len(output)+1))

input('Pressione enter para continuar')