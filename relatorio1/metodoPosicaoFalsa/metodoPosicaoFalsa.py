###########################################
# Matéria: Análise Numérica
# Autor: Levy Marlon Souza Santiago
# Matrícula: 201520138
# Turma: 2015.2
###########################################

from sympy import *
import sys

#Variáveis gerais a serem usadas
#A função de entrada
funcao = None
#As outras entradas tipo o intervalo e a precisao
entradas = None
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

def calculaMeio(a, b):
	#Cálculo do meio a partir do método
	return b - ((f(b)*(b - a))/(f(b) - f(a)));

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
	global funcao, arqEntrada, entradas
	
	#Definindo a função obtida pelo arquivo e retirando o '\n'
	funcao = arqEntrada.readline().split('\n')[0]

	#Criando um dicionario com as pŕóximas entradas
	entradas = {}
	entradas['inicio'] = float(arqEntrada.readline().split('\n')[0])
	entradas['fim'] = float(arqEntrada.readline().split('\n')[0])
	entradas['precisao'] = float(arqEntrada.readline().split('\n')[0])

	#Retirando linha \n ou '' (fim do arquivo)
	linha = arqEntrada.readline()
	
	return linha

def metodoPosicaoFalsa(inicio, fim, precisao, f):
	#Calculando o f do inicio e fim do intervalo
	fInicio = f(inicio)
	fFim = f(fim)

	#Se a precisao for maior do que f(inicio) e maior f(fim), não é possivel continuar
	if(abs(fInicio) > precisao or abs(fFim) > precisao):
		#Calculando o meio do intervalo, e o f(meio)
		meio = calculaMeio(inicio, fim)
		fMeio = f(meio)

		#Repetimos o processo até que abs(fMeio) seja <= à precisao
		while(abs(fMeio) > precisao):
			#Se o sinal de fInicio e fMeio são diferentes
			if(fInicio * fMeio < 0):
				fim = meio
			#Se o sinal de fInicio e fMeio são iguais
			else:
				inicio = meio
				fInicio = fMeio
			#Calculando o meio do intervalo, e o f(meio)
			meio = calculaMeio(inicio, fim)
			fMeio = f(meio)
		return float(meio)
	else:
		return None

def main():
	global funcao, arqSaida, entradas

	#Abrindo os arquivos de entrada e saida
	abrirArquivos()

	#Enquanto existirem dados a serem lidos
	while(True):
		#Obtendo os primeiros dados do arquivo de Entrada
		fim = lerArquivo()

		#Executando o metodo da Posicao Falsa
		resultado = metodoPosicaoFalsa(entradas['inicio'], entradas['fim'], entradas['precisao'], f)
		
		#Se resultado retorna None, ocorreu um erro nos intervalos
		if(resultado != None):
			#Testando o resultado
			resultTestado = f(resultado)
			#Obtendo o valor absoluto
			resultTestado = abs(resultTestado)

			#Se o resultado está perto de 0
			if(resultTestado >= 0 and resultTestado < 1):
				#Imprimindo dados no arquivo de saida
				arqSaida.write("F(x) = ")
				arqSaida.write(funcao)
				arqSaida.write("\n")
				arqSaida.write("\n\tRaiz ~= ")
				arqSaida.write(str(resultado))
				arqSaida.write("\n")
				arqSaida.write("\n\tF(Raiz) = ")
				arqSaida.write(str(resultTestado))
				arqSaida.write("\n\n")
				
			else:
				arqSaida.write("Deu errado.\n")
		else:
			arqSaida.write("\nVerifique se os intervalos estão corretos.\n")

		#Se esta foi a ultima entrada
		if(fim == ''):
			break;
	
	#Fechando arquivos de entrada e saida
	fecharArquivos()

main()