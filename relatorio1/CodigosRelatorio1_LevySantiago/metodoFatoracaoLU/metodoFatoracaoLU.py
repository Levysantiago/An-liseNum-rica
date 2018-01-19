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
#As equações a serem usadas
equacoes = None
#Os valores das igualdades das equações, vetor B
vetB = None
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
	global arqEntrada, equacoes, vetB, qtdEquacoes
	
	#Criando uma lista para as equacoes
	equacoes = []
	#Criando uma lista para o vetor B
	vetB = []
	#Lendo primeira linha do arquivo
	linha = arqEntrada.readline()
	#Enquanto estiver lendo as equações
	while(linha != '' and linha != '\n'):
		#Primeira parte da equação (antes do '=')
		equacoes.append(linha.split('=')[0])
		#Segunda parte da equação (depois do '=')
		vetB.append(linha.split('=')[1])

		#Lendo proxima linha
		linha = arqEntrada.readline()
	#Calculando a quantidade de equações
	qtdEquacoes = equacoes.__len__()

	return linha

def gerarMatrizEquacoes(equacoes):
	global qtdEquacoes

	#Criando uma lista inicial
	matriz = []
	for i in range(0,qtdEquacoes):
		#Recebendo a equação e transformando em um tipo polinomial
		aux = Poly(equacoes[i], x, y, z)
		#Obtendo uma lista dos coeficientes do polinomio e inserindo como linhas da matriz
		matriz.append(aux.coeffs())

	return matriz

def gerarMatrizQuad(tam):
	#Criando uma lista inicial
	matriz = []
	#Criando uma matriz quadrada e inicializando com 0
	for i in range(tam):
		#Inserindo tam listas
	    matriz.append([0] * tam)

	return matriz
	

def metodoFatoracaoLU(equacoes, vetB, variaveis):
	global qtdEquacoes

	#Criando matriz com os coeficientes da equacao
	matriz = gerarMatrizEquacoes(equacoes)

	#Gerando matriz L e U em uma mesma matriz
	matrizLU = gerarMatrizQuad(qtdEquacoes)

	#Iniciando calculo dos termos da matriz LU
	i = j = 0
	while(i < qtdEquacoes and j < qtdEquacoes):
		#Calculando a parte U
		for j in range(i, qtdEquacoes):
			somatorio = 0
			#Aplicação da fórmula: Uij = Aij - Somatorio(k=1 até i-1 de Lik * Ukj)
			for k in range(0, i):
				somatorio += matrizLU[i][k] * matrizLU[k][j]
			matrizLU[i][j] = matriz[i][j] - somatorio

		#Calculando a parte L
		for j in range(i+1, qtdEquacoes):
			somatorio = 0
			#Aplicação da fórmula: Lij = (Aij - Somatorio(k=1 até j-1 de Lik * Ukj)) / Ujj
			#Porém, como tudo foi feito em um mesmo while, então podemos usar o j como linha e o i como coluna
			for k in range(0, i):
				somatorio += matrizLU[j][k] * matrizLU[k][i]
			matrizLU[j][i] = (matriz[j][i] - somatorio)	/ matrizLU[i][i]
		
		i += 1
	
	#Criando um vetor multiplicador
	vetMultiplicador = [0]*qtdEquacoes

	#Criando uma lista de variáveis auxiliares
	tupAuxVar = list(symbols('a b c d e'))

	#MULTIPLICAÇÃO L * VETOR_Y = B
	for i in range(0, qtdEquacoes):
		#Inicializando o vetor multiplicador com cada linha da matriz até i
		for j in range(0, i):
			vetMultiplicador[j] = matrizLU[i][j]
		#Valor da diagonal é sempre 1 na matriz L, ou seja, quando j = i
		vetMultiplicador[j] = 1

		#Iniciando multiplicação pela matriz L
		aux = 0
		for j in range(0, qtdEquacoes):
			aux += vetMultiplicador[j] * tupAuxVar[j]
		#Substituindo o valor do vetor B na equação resultante
		vetB[i] = solve_linear(aux, vetB[i])

		#Trocando a variavel por seu valor encontrado
		tupAuxVar[i] = tupAuxVar[i].subs(tupAuxVar[i], vetB[i][1]) #[1] por que a tupla gerada é do tipo (variavel, valor)
		#Usando o vetor B para receber o valor da variável, para gerar os proximos calculos
		vetB[i] = tupAuxVar[i]

	#Reiniciando matriz multiplicadora com 0
	for j in range(0, qtdEquacoes):
		vetMultiplicador[j] = 0

	#MULTIPLICAÇÃO U * VETOR_X = VETY
	#Desta vez vamos da ultima linha para a primeira
	for i in range(qtdEquacoes-1, -1, -1):
		#Inicializando o vetor multiplicador com cada linha da matriz de i até o fim
		#Os valores anteriores a i, ficam com 0, e é o que queremos
		for j in range(i, qtdEquacoes):
			vetMultiplicador[j] = matrizLU[i][j]

		#Iniciando multiplicação da matriz U e as variáveis do sistema
		aux = 0
		for j in range(0, qtdEquacoes):
			aux += vetMultiplicador[j] * variaveis[j]
		#Substituindo o valor do vetor B na equação resultante
		vetB[i] = solve_linear(aux, vetB[i])

		#Trocando a variavel por seu valor encontrado
		variaveis[i] = variaveis[i].subs(variaveis[i], vetB[i][1])

	#No fim, o vetor B será uma lista de tuplas (variavel, valor), e assim mesmo ele foi retornado
	return vetB

def main():
	global arqSaida, equacoes, vetB

	#Abrindo os arquivos de entrada e saida
	abrirArquivos()

	#Enquanto existirem dados a serem lidos
	while(True):
		#Obtendo os primeiros dados do arquivo de Entrada
		fim = lerArquivo()

		#Transformando as equações de string para expressão
		for i in range(0, qtdEquacoes):
			equacoes[i] = eval(equacoes[i])
			vetB[i] = eval(vetB[i])

		#Definindo as variáveis do sistema
		variaveis = [x, y, z, w, g]

		#Executando o método Fatoração LU
		resultado = metodoFatoracaoLU(equacoes, vetB, variaveis)

		#Imprimindo resultado no arquivo de saida
		for i in range(0, qtdEquacoes):
			arqSaida.write(str(resultado[i]))
			arqSaida.write("\n")
		arqSaida.write("\n")

		#Se esta foi a ultima entrada
		if(fim == ''):
			break;
	
	#Fechando arquivos de entrada e saida
	fecharArquivos()

main()
