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
#A precisao da resposta
precisao = None
#O valor inicial para a iteração
valorInicial = None
#As equações de entrada
equacoes = None
#Os arquivos de entrada e saida
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
	global arqEntrada, equacoes, valorInicial, precisao
	linha = None;
	equacoes = []

	#Lendo a precisao e transformando em float
	precisao = float(arqEntrada.readline().split('\n')[0])
	#Lendo o valor inicial e transformando para float
	valorInicial = float(arqEntrada.readline().split('\n')[0])
	#Lendo próxima linha (inicio das equações)
	linha = arqEntrada.readline()
	#Enquanto estiver lendo as equações
	while(linha != '' and linha != '\n'):
		#Guardando as equacoes
		equacoes.append(linha.split('\n')[0])
		#Lendo proxima linha
		linha = arqEntrada.readline()

	return linha

def metodoPontoFixo(precisao, x0, equacoes, f):
	global funcao, arqSaida
	
	#Calculando a quantidade de equações
	qtdEquacoes = equacoes.__len__()
	for i in range(0, qtdEquacoes):
		#Setando uma função para o calculo do f(x)
		funcao = equacoes[i]
		#Se existir raiz na função, pode resultar em numeros complexos
		if(funcao.count("sqrt") < 1):
			#Valor inicial recebido
			x = x0
			#Inicializando variavel para guardar o valor anterior de x
			xAnt = 0
			#Enquanto o valor absoluto da diferença entre x e o seu valor anterior for > precisao
			while(abs(x - xAnt) > precisao):
				#Guardando o valor de x
				xAnt = x
				#Calculando o valor de f(x), de acordo com a função setada anteriormente
				x = f(x)

			#Inserindo no arquivo os resultados de cada equação
			arqSaida.write("Equacao: ")
			arqSaida.write(funcao)
			arqSaida.write("\n")
			arqSaida.write("	Valor: ")
			arqSaida.write(str(float(abs(x))))
			arqSaida.write("\n\n")
		else:
			arqSaida.write("Função com raiz pode não convergir.\n")

def main():
	global arqSaida, equacoes, valorInicial, precisao

	#Abrindo os arquivos de entrada e saida
	abrirArquivos()

	#Enquanto existirem dados a serem lidos
	while(True):
		#Obtendo os dados do arquivo de Entrada
		fim = lerArquivo()

		#Executando o metodo do Ponto Fixo
		resultado = metodoPontoFixo(precisao, valorInicial, equacoes, f)

		#Separando os resultados de outras entradas
		arqSaida.write("\n\n")

		#Se esta foi a ultima entrada
		if(fim == ''):
			break

	#Fechando arquivos de entrada e saida
	fecharArquivos()
	
main()



