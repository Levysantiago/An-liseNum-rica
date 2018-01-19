###########################################
# Matéria: Análise Numérica
# Autor: Levy Marlon Souza Santiago
# Matrícula: 201520138
# Turma: 2015.2
###########################################

from sympy import *
import sys

#Variáveis gerais a serem usadas

#Vetor de entrada dos valores de x
xi = None
#Vetor de entrada dos valores de f(x)
fx = None
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
	global arqEntrada, fx, xi, base

	fx = []
	xi = []
	base = []

	#Lendo os valores de x
	aux = arqEntrada.readline()
	while(aux != '' and aux != '\n'):
		aux = float(aux)
		xi.append(aux)
		aux = arqEntrada.readline()
	
	#Lendo os valores da função
	aux = arqEntrada.readline()
	while(aux != '' and aux != '\n'):
		aux = float(aux)
		fx.append(aux)
		aux = arqEntrada.readline()

	#Lendo a base do sub-espaço
	aux = arqEntrada.readline()
	while(aux != '' and aux != '\n'):
		base.append(eval(aux))
		aux = arqEntrada.readline()

	linha = arqEntrada.readline()

	return linha

def somaElementos(vet, n):
	soma = 0.0

	for i in range(n):
		soma += vet[i]

	return soma

def multiVetores(vet1, vet2, n):
	r = []
	for i in range(n):
		r.append(vet1[i] * vet2[i])
	return r 

def mmqDiscreto(fx, xi, base):
	tamBase = len(base)
	tamXi = len(xi)
	matrizRes = zeros(tamBase)
	vetorF = zeros(tamBase, 1)
	matrizUi = [tamXi*[1]]
	count = 0

	#Gerando os vetores u0, u1, ..., un
	listaAux = []
	for i in range(tamBase):
		aux = base[i]
		if(aux != 1):
			for elem in xi:
				listaAux.append(aux.subs(x, elem))
			matrizUi.append(listaAux)
			listaAux = []
	
	#Gerando a matriz para o calculo do sistema
	for i in range(tamBase):
		for j in range(tamBase):
			matrizRes[i,j] = somaElementos(multiVetores(matrizUi[i], matrizUi[j], tamXi), tamXi)
		vetorF[i] = somaElementos(multiVetores(fx, matrizUi[i], tamXi), tamXi)

	#Usando fatoração LU para resolver o sistema
	resultado = matrizRes.LUsolve(vetorF)

	#Criando a equação final a partir do resultado
	simb = 1
	result = 0
	for i in range(tamBase):
		result += round(resultado[i,0], 3)*simb
		simb *= x

	return result

def main():
	global arqSaida, fx, xi, base

	#Abrindo os arquivos de entrada e saida
	abrirArquivos()

	while(True):
		fim = lerArquivo()

		#Aplicando o método
		resultado = mmqDiscreto(fx, xi, base)

		#Imprimindo no arquivo de saida
		arqSaida.write("\nf(x) ~= ")
		arqSaida.write(str(resultado))
		arqSaida.write("\n")

		if(fim == ''):
			break
	#Fechando arquivos
	fecharArquivos()

main()
