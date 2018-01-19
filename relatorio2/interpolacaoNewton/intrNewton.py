###########################################
# Matéria: Análise Numérica
# Autor: Levy Marlon Souza Santiago
# Matrícula: 201520138
# Turma: 2015.2
###########################################

from sympy import *
import sys

#Variáveis gerais a serem usadas
#Os valores para f(x)
fn = None
#Os valores para os pontos
xn = None
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
	global arqEntrada, fn, xn
	fn = {}
	xn = []

	#Lendo os valores da função
	aux = arqEntrada.readline()
	
	while(aux != '' and aux != '\n'):
		aux = float(aux)
		xn.append(aux)
		aux = arqEntrada.readline()
	aux = arqEntrada.readline()
	i = 0
	while(aux != '' and aux != '\n'):		
		aux = float(aux)
		fn[xn[i]] = aux		
		i += 1
		aux = arqEntrada.readline()
	

	linha = arqEntrada.readline()

	return linha
	
def calculaF(fn, xn):
	n = len(xn)
	if(n == 1):
		return fn[xn[0]]
	if(n == 2):
		return (fn[xn[0]] - fn[xn[1]]) / (xn[0] - xn[1])
	else:		
		return (calculaF(fn, xn[0 : n-1]) - calculaF(fn, xn[1 : n])) / (xn[0] - xn[n-1])

def intrNewton(fn, xn):
	termos = 1
	n = len(xn)
	P = 0
	xAux = []

	for i in range(n):
		xAux.append(xn[i])
		P += termos * round(calculaF(fn, xAux), 2)
		termos *= Poly(x - xn[i])

	return str(P.args[0])


def main():
	global arqSaida, fn, xn

	#Abrindo os arquivos de entrada e saida
	abrirArquivos()

	while(True):
		fim = lerArquivo()

		#Aplicando o método
		resultado = intrNewton(fn, xn)

		#Imprimindo no arquivo de saida
		arqSaida.write("\nP(x) = ")
		arqSaida.write(resultado)
		arqSaida.write("\n")

		if(fim == ''):
			break
	#Fechando arquivos
	fecharArquivos()

main()
