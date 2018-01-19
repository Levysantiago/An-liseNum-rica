###########################################
# Matéria: Análise Numérica
# Autor: Levy Marlon Souza Santiago
# Matrícula: 201520138
# Turma: 2015.2
###########################################

from sympy import *
import sys

#Variáveis gerais a serem usadas
#A função f(x)
fx = None
#O intervalo de integração como um dicionário
intervalo = None
#Número de subintervalos
nSubIntervalos = None
#Definindo o símbolo x
x = symbols('x')
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
	global arqEntrada, fx, intervalo, nSubIntervalos

	intervalo = {}
	base = []

	#Lendo a função
	fx = eval(arqEntrada.readline())

	#Lendo \n
	arqEntrada.readline()

	#Lendo o intervalo de integração
	intervalo['inicio'] = float(arqEntrada.readline())
	intervalo['fim'] = float(arqEntrada.readline())

	#Lendo \n
	arqEntrada.readline()

	#Lendo a base do sub-espaço
	nSubIntervalos = int(arqEntrada.readline())

	#Lendo \n
	arqEntrada.readline()

	linha = arqEntrada.readline()

	return linha

def gerarIntervalos(inicio, fim, h):
	xi = [inicio]

	aux = inicio + h
	while(aux != fim):
		aux = round(aux, 2)
		xi.append(aux)
		aux += h
	xi.append(aux)
	return xi

def metodoTrapezio(fx, intervalo, n):
	h = (intervalo['fim'] - intervalo['inicio']) / n
	xi = gerarIntervalos(intervalo['inicio'], intervalo['fim'], h)
	tam = len(xi)
	I = fx.subs(x, intervalo['inicio']) + fx.subs(x, intervalo['fim'])

	#Calculando f(x) para cada intervalo
	for i in range(1,tam-1):
		I += 2*(fx.subs(x, xi[i]))
	I *= h/2
	return round(I, 3)

def main():
	global arqSaida, fx, intervalo, nSubIntervalos

	#Abrindo os arquivos de entrada e saida
	abrirArquivos()

	while(True):
		fim = lerArquivo()

		#Aplicando o método
		resultado = metodoTrapezio(fx, intervalo, nSubIntervalos)

		#Imprimindo no arquivo de saida
		arqSaida.write("\nI(f(x)) ~= ")
		arqSaida.write(str(resultado))
		arqSaida.write("\n")

		if(fim == ''):
			break
	#Fechando arquivos
	fecharArquivos()

main()
