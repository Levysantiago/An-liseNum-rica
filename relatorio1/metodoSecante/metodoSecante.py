###########################################
# Matéria: Análise Numérica
# Autor: Levy Marlon Souza Santiago
# Matrícula: 201520138
# Turma: 2015.2
###########################################

import sys
from sympy import *

funcao = None
precisao = None
valoresIniciais = None

arqEntrada = None
arqSaida = None

def f(x):
	global arqSaida

	#Se não existe 'x' na string 'funcao', então a função é contínua
	if(funcao.count('x') < 1):
		arqSaida.write("\nERRO! Função contínua.\n")
		exit()
	#Se a funcao recebeu alguma informação
	elif(funcao != None and funcao != ''):
		return eval(funcao)
	else:
		arqSaida.write("ERRO! Função inválida!!")
		exit()

def abrirArquivo():
	global arqEntrada

	#Se não foi dado um segundo argumento
	if(len(sys.argv) < 2):
		print("Insira no argumento o nome do arquivo.\n")
		exit()

	#Abrindo o arquivo de entrada
	arqEntrada = open(sys.argv[1], "r")

def fecharArquivo():
	global arqEntrada

	if(arqEntrada != None):
		arqEntrada.close()

def lerArquivo():
	global funcao, arqEntrada, precisao, valoresIniciais

	valoresIniciais = []

	#Definindo a função obtida pelo arquivo
	funcao = arqEntrada.readline().split('\n')[0]

	#Obtendo a precisao
	precisao = float(arqEntrada.readline().split('\n')[0])

	#Obtendo o valor inicial
	valoresIniciais.append(float(eval(arqEntrada.readline().split('\n')[0])))
	valoresIniciais.append(float(eval(arqEntrada.readline().split('\n')[0])))

	#Linha \n
	linha = arqEntrada.readline()

	return linha

def getArquivoSaida():
	saida = open("saida.txt", "w")
	if(saida == None):
		print("Erro ao abrir arquivo de saida.\n")
		exit()
	return saida

def metodoSecante(precisao, x0, x1, f):
	#Definindo o x como um símbolo
	xSymbol = symbols('x')

	#Calculando a derivada de f
	fD = diff(f(xSymbol), xSymbol)

	#Inicializando valor x0 e x1
	xAnt = x0
	x = x1

	while(abs(x - xAnt) > precisao):
		#Guardando valor anterior de x
		aux = x

		#Obtendo o resultado das iterações
		x = (xAnt*f(x) - x*f(xAnt)) / (f(x) - f(xAnt))

		#Guardando valor anterior de x
		xAnt = aux

	return float(x)

def main():
	global funcao, arqSaida, precisao, valoresIniciais

	#Abrindo o arquivo de entrada
	abrirArquivo()

	#Abrindo arquivo de saida
	arqSaida = getArquivoSaida()

	while(True):
		#Obtendo os dados do arquivo de Entrada
		fim = lerArquivo()

		#Executando o metodo do Ponto Fixo
		resultado = metodoSecante(precisao, valoresIniciais[0], valoresIniciais[1], f)

		arqSaida.write("F(x) = ")
		arqSaida.write(funcao)
		arqSaida.write("\n")
		arqSaida.write("	Resultado: ")
		arqSaida.write(str(resultado))
		arqSaida.write("\n\n")

		if(fim == ''):
			break

	#Fechando arquivo de entrada
	fecharArquivo()

	#Fechando arquivo de saida
	arqSaida.close()
	
main()



