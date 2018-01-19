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
#Base de Sub-espaço
base = None
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
	global arqEntrada, fx, intervalo, base

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
	aux = arqEntrada.readline()
	while(aux != '' and aux != '\n'):
		base.append(eval(aux))
		aux = arqEntrada.readline()

	linha = arqEntrada.readline()

	return linha

def mmqContinuo(fx, intervalo, base):
	tamBase = len(base)
	matrizAux = zeros(tamBase)
	vetorF = zeros(tamBase, 1)
	count = 0

	for i in range(tamBase):
		aux = base[i]*fx
		vetorF[i,0] = integrate(aux, (x, intervalo['inicio'], intervalo['fim']))
		for j in range(tamBase):
			aux = base[i]*base[j]
			matrizAux[i,j] = aux
			count += 1

			if(count == tamBase):
				for count in range(tamBase):
					matrizAux[i,count] = integrate(matrizAux[i,count], (x, intervalo['inicio'], intervalo['fim']))
				count = 0

	#Usando fatoração LU para resolver o sistema
	resultado = matrizAux.LUsolve(vetorF)

	#Criando a equação final a partir do resultado
	simb = 1
	result = 0
	for i in range(tamBase):
		result += round(resultado[i,0], 3)*simb
		simb *= x

	return result


def main():
	global arqSaida, fx, intervalo, base

	#Abrindo os arquivos de entrada e saida
	abrirArquivos()

	while(True):
		fim = lerArquivo()

		#Aplicando o método
		resultado = mmqContinuo(fx, intervalo, base)

		#Imprimindo no arquivo de saida
		arqSaida.write("\nf(x) ~= ")
		arqSaida.write(str(resultado))
		arqSaida.write("\n")

		if(fim == ''):
			break
	#Fechando arquivos
	fecharArquivos()

main()
