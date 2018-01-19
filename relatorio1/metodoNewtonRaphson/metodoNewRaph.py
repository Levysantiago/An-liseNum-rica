###########################################
# Matéria: Análise Numérica
# Autor: Levy Marlon Souza Santiago
# Matrícula: 201520138
# Turma: 2015.2
###########################################

import sys
from sympy import *

#Variáveis gerais a serem usadas
#Recebe uma função qualquer 
funcao = None
#A precisão para a resposta
precisao = None
#O valor inicial da iteração
valorInicial = None

#Arquivos de entrada e saida
arqEntrada = None
arqSaida = None

def f(x):
	global funcao, arqSaida

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
	global funcao, arqEntrada, precisao, valorInicial
	
	#Definindo a função obtida pelo arquivo
	funcao = arqEntrada.readline().split('\n')[0]

	#Obtendo a precisao
	precisao = float(arqEntrada.readline().split('\n')[0])

	#Obtendo o valor inicial
	valorInicial = float(eval(arqEntrada.readline().split('\n')[0]))

	#Linha '\n' ou '' (fim de arquivo)
	linha = arqEntrada.readline()

	return linha

def metodoNewRaph(precisao, x0, f):
	#Definindo o x como um símbolo para o calculo da derivada
	xSymbol = symbols('x')

	#Calculando a derivada de f em relação a x
	fD = diff(f(xSymbol), xSymbol)

	#Definindo o valor inicial
	x = x0

	#Inicializando valor anterior de x
	xAnt = 0

	#Obtendo o resultado da primeira substituição (xSymbol = x e x = valor de x0)
	x = x - (f(x) / fD.subs(xSymbol, x))

	#Enquanto o valor absoluto da diferença entre x e o seu valor anterior for > precisao
	while(abs(x - xAnt) > precisao):
		#Guardando valor anterior de x
		xAnt = x

		#Obtendo o resultado das iterações
		x = x - (f(x) / fD.subs(xSymbol, x))

	return float(x)

def main():
	global funcao, arqSaida, precisao

	#Abrindo os arquivos de entrada e saida
	abrirArquivos()

 	#Enquanto existirem dados a serem lidos
	while(True):
		#Obtendo os dados do arquivo de Entrada
		fim = lerArquivo()

		#Executando o metodo de Newton Raphson
		resultado = metodoNewRaph(precisao, valorInicial, f)

		arqSaida.write("F(x) = ")
		arqSaida.write(funcao)
		arqSaida.write("\n")
		arqSaida.write("	Resultado: ")
		arqSaida.write(str(resultado))
		arqSaida.write("\n\n")

		#Se esta foi a ultima entrada
		if(fim == ''):
			break

	#Fechando arquivos de entrada e saida
	fecharArquivos()
	
main()



