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

	#Criando uma lista das equacoes e do vetor B
	equacoes = []
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

def gerarMatriz(equacoes, variaveis):
	global qtdEquacoes

	#Criando uma lista inicial
	matriz = []
	for i in range(0,qtdEquacoes):
		#Recebendo a equação e transformando em um tipo polinomial
		aux = Poly(equacoes[i], variaveis)
		#Obtendo uma lista dos coeficientes do polinomio e inserindo como linhas da matriz
		matriz.append(aux.coeffs())

	return matriz
	

def metodoElGauss(equacoes, vetB, variaveis):
	global qtdEquacoes

	#Criando matriz com os coeficientes da equacao
	matriz = gerarMatriz(equacoes, variaveis)

	#Transformando a matriz em triangular
	#Vamos caminhar primeiro as linhas, depois as colunas
	for j in range(0, qtdEquacoes):
		#Determinando o pivo
		pivo = matriz[j][j]
		#Vamos sempre começar de j+1 pois queremos zerar os elementos abaixo do elemento da diagonal
		for i in range(j+1, qtdEquacoes):
			if(pivo != 0):
				#Calculando o multiplicador
				m = matriz[i][j] / pivo
				#Calculando e substituindo os valores abaixo dos valores da diagonal de acordo com o método
				for c in range(0,qtdEquacoes):
					matriz[i][c] = matriz[i][c] - m * matriz[j][c]
				#Atualizando vetor 'b'
				vetB[i] = vetB[i] - m * vetB[j]
			else:
				#Se o pivo for 0, então trocamos com a linha de baixo
				if(j < qtdEquacoes):
					for i in range(0, qtdEquacoes):
						aux = matriz[j][i]
						matriz[j][i] = matriz[j+1][i]
						matriz[j+1][i] = aux
					aux = vetB[j]
					vetB[j] = vetB[j+1]
					vetB[j+1] = aux

	#Criando uma lista, a qual será o resultado
	results = []
	#Contador para a lista results, pois os outros contadores contam ao contrário
	r = 0
	#Vamos caminhar pela matriz da ultima linha para a primeira, pois 
	for i in range(qtdEquacoes -1, -1, -1):
		#Setando a equação como 0, pois vamos a usar como uma variável de somatório
		equacoes[i] = 0
		#Caminhando as colunas também do final para o começo
		for j in range(qtdEquacoes -1, -1, -1):
			#Reconstruindo a equação a partir da nova matriz
			equacoes[i] += matriz[i][j] * variaveis[j]
		#Resolvendo as equações
		results.append(solve_linear(equacoes[i], vetB[i]))
		#Substituindo a variável por seu valor encontrado. results[r][1] pois results[r] = (variavel, valor), e queremos somente o valor
		variaveis[i] = variaveis[i].subs(variaveis[i], results[r][1])
		r += 1

	return results

def main():
	global arqSaida, equacoes, vetB, variaveis

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

		#Executando o método Eliminação de Gauss
		resultado = metodoElGauss(equacoes, vetB, variaveis)

		#Imprimindo o resultado no arquivo
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
