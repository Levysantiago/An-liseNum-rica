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

"""
TOMANDO:
	c1 = 0
	c2 = 1
	a2 = 1/2

	yn+1 = yn + h*k2
	k1 = f(xn,yn)
	k2 = f(xn + (1/2)*h, yn + (1/2)*h*k1)
	Método de Euler Modificado

"""

def metodoRungeKutta2(f, yi, intervalo, h):
	xi = 0
	k1 = k2 = f
	saida = {}
	while(xi < intervalo['fim']):
		#Calculando k1
		k1_val = k1.subs(x, xi)
		k1_val = k1_val.subs(y, yi)

		#Calculando k2
		k2_val = k2.subs(x, (xi + (0.5)*h))
		k2_val = k2_val.subs(y, yi + (0.5)*h*k1_val)

		#Atualizando o yi
		yi = yi + h * k2_val

		#Aproximando o valor em 3 casas decimais
		yi = round(yi, 3)

		saida[xi] = yi

		#Atualizando o xi
		xi = round(xi + h, 2)

	return saida
	

def main():
	global arqSaida, yd, intervalo, y0, h

	#Abrindo os arquivos de entrada e saida
	abrirArquivos()

	while(True):
		fim = lerArquivo()

		#Aplicando o método
		resultado = metodoRungeKutta2(yd, y0, intervalo, h)

		#Imprimindo no arquivo de saida
		arqSaida.write("\nResultado = ")
		arqSaida.write(str(resultado))
		arqSaida.write("\n")

		if(fim == ''):
			break
	#Fechando arquivos
	fecharArquivos()
	
main()
