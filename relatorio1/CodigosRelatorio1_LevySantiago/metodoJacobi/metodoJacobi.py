###########################################
# Matéria: Análise Numérica
# Autor: Levy Marlon Souza Santiago
# Matrícula: 201520138
# Turma: 2015.2
###########################################

from sympy import *
import sys

#Definindo os símbolos
x, y, z, w, g = symbols('x y z w g')

#Variáveis gerais a serem usadas
#A quantidade de equações
qtdEquacoes = None
#As equações do sistema
equacoes = None
#A precisao para a resposta
precisao = None

#Arquivos de entrada e saida
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
	global arqEntrada, equacoes, precisao, qtdEquacoes
	
	#Criando uma lista para equacoes
	equacoes = []

	#Primeira linha é a precisao em níveis
	precisao = int(arqEntrada.readline())

	#Lendo primeira linha do arquivo
	linha = arqEntrada.readline()
	#Enquanto estiver lendo as equações
	while(linha != '' and linha != '\n'):
		#Lendo uma equação
		linha = linha.split('=')
		#Inserindo as equações na lista
		equacoes.append(Eq(eval(linha[0]), float(eval(linha[1]))))

		#Lendo proxima linha
		linha = arqEntrada.readline()
	#A quantidade de equações
	qtdEquacoes = equacoes.__len__()

	return linha

def converge(equacoes, qtdEquacoes):
	flag = True
	for i in range(0, qtdEquacoes):
		#Recebendo os coeficientes de uma equação
		coeficientes = Poly(equacoes[i].lhs).coeffs()
		soma = 0
		for j in range(0, qtdEquacoes):
			#Fazendo o somatório de todos os elementos fora da diagonal
			if(i != j):
				soma += abs(coeficientes[j])
		#Se a soma for maior do que o valor absoluto do elemento da diagonal, o sistema não converge
		if(soma > abs(coeficientes[i])):
			flag = False
			break
	return flag

def metodoJacobi(equacoes, variaveis, precisao):
	#Calculando a quantidade de equações
	qtdEquacoes = equacoes.__len__()
	#Vetor usado para fazer os calculos
	vetAux = None
	#Vetor de resposta
	vetResultado = None
	
	#Se a função converge, então pode continuar
	if(converge(equacoes, qtdEquacoes)):
		#Inicializando vetor Resultado
		vetResultado = [0]*qtdEquacoes

		#Isolando cada variavel de acordo com cada equação
		for i in range(0, qtdEquacoes):
			equacoes[i] = solve_linear(equacoes[i], symbols = [variaveis[i]])

		#Fazendo os calculos de acordo com o nível máximo de precisao
		for parada in range(0, precisao):
			#Fazendo uma cópia do vetor resultado para usar como entrada
			vetAux = vetResultado[:]
			for i in range(0, qtdEquacoes):
				#Iniciando substituições, o vetor resultado recebe uma equação
				vetResultado[i] = equacoes[i][1]
				for j in range(0, qtdEquacoes):
					#Se existe uma dada variável na equação, então pode-se substituir o valor
					if(vetResultado[i].has(variaveis[j])):
						#Substituindo e atribuindo o valor para a posição no vetor resultado
						vetResultado[i] = vetResultado[i].subs(variaveis[j], vetAux[j])
		#Arredondando os resultados para 2 casas decimais
		for i in range(0, qtdEquacoes):
			vetResultado[i] = round(vetResultado[i], 2)

	return vetResultado

def main():
	global arqSaida, equacoes, precisao, qtdEquacoes

	#Abrindo os arquivos de entrada e saida
	abrirArquivos()

	#Enquanto existirem dados a serem lidos
	while(True):
		#Obtendo os primeiros dados do arquivo de Entrada
		fim = lerArquivo()

		#Definindo as variáveis do sistema
		variaveis = [x, y, z, w, g]

		#Executando o método de Jacobi
		resultado = metodoJacobi(equacoes, variaveis, precisao)

		if(resultado != None):
			for i in range(0, qtdEquacoes):
				arqSaida.write(str(resultado[i]))
				arqSaida.write("\n")
		else:
			arqSaida.write("Não converge.\n")
		arqSaida.write("\n")

		if(fim == ''):
			break;
	
	#Fechando arquivos de entrada e saida
	fecharArquivos()

main()
