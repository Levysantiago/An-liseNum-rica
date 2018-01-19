###########################################
# Matéria: Análise Numérica
# Autor: Levy Marlon Souza Santiago
# Matrícula: 201520138
# Turma: 2015.2
###########################################

from sympy import *
import sys

#Variáveis gerais a serem usadas
#A função y' (derivada a primeira)
yd = None
#O intervalo da solução como um dicionário
intervalo = None

#O valor de y(0)
y0 = None

#O valor de h
h = None

y,x = symbols('y x')
#Os arquivos de entrada e saida
arqEntrada = None
arqSaida = None

def abrirArquivos():
	global arqEntrada, arqSaida

	#Se não foi dado um segundo argumento
	if(len(sys.argv) < 2):
		print("Insira no argumento o nome do arquivo.\n")
		exit()

	#Abrindo o arquivo de entrada
	arqEntrada = open(sys.argv[1], "r")
	if(arqEntrada == None):
		print("Erro ao abrir arquivo de entrada.\n")
		exit()

	#Abrindo o arquivo de saida
	arqSaida = open("saida.txt", "w")
	if(arqSaida == None):
		print("Erro ao abrir arquivo de saida.\n")
		exit()

def fecharArquivos():
	global arqEntrada, arqSaida

	#Fechando arquivo de entrada
	if(arqEntrada != None):
		arqEntrada.close()
		arqEntrada = None
	#Fechando arquivo de saida
	if(arqSaida != None):
		arqSaida.close()
		arqSaida = None

def lerArquivo():
	global arqEntrada, yd, intervalo, y0, h

	intervalo = {}

	#Lendo a função
	yd = eval(arqEntrada.readline())

	#Lendo \n
	arqEntrada.readline()

	y0 = float(arqEntrada.readline())

	#Lendo \n
	arqEntrada.readline()

	#Lendo o intervalo de integração
	intervalo['inicio'] = float(arqEntrada.readline())
	intervalo['fim'] = float(arqEntrada.readline())

	#Lendo \n
	arqEntrada.readline()

	#Lendo a base do sub-espaço
	h = float(arqEntrada.readline())

	#Lendo \n
	arqEntrada.readline()

	linha = arqEntrada.readline()

	return linha

def metodoHeun(f, yi, intervalo, h):
	xi = 0
	while(xi < intervalo['fim']):
		#Substituindo os valores de xi e yi em f
		f_val = f.subs(x, xi)
		f_val = f_val.subs(y, yi)

		#Aplicando o método e atualizando o yi
		yAnt = yi
		yi = yAnt + f_val * h

		#Atualizando o xi
		xi = round(xi + h, 2)

		#Guardando substituição anterior
		f_valAnt = f_val

		#Substituindo os valores de xi+1 e yi+1 em f
		f_val = f.subs(x, xi)
		f_val = f_val.subs(y, yi)

		#Aplicando o método e atualizando o yi com a media
		yi = yAnt + ((f_valAnt + f_val)/2)*h

	#Aproximando o valor em 3 casas decimais
	yi = round(yi, 3)

	return yi
	

def main():
	global arqSaida, yd, intervalo, y0, h

	#Abrindo os arquivos de entrada e saida
	abrirArquivos()

	while(True):
		fim = lerArquivo()

		#Aplicando o método
		resultado = metodoHeun(yd, y0, intervalo, h)

		#Imprimindo no arquivo de saida
		arqSaida.write("\nResultado = ")
		arqSaida.write(str(resultado))
		arqSaida.write("\n")

		if(fim == ''):
			break
	#Fechando arquivos
	fecharArquivos()
	
main()
