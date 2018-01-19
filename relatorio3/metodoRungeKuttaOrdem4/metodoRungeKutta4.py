###########################################
# Matéria: Análise Numérica
# Autor: Levy Marlon Souza Santiago
# Matrícula: 201520138
# Turma: 2015.2
###########################################

from sympy import *
import sys

#Variáveis gerais a serem usadas
#A função y' (derivada a primeira)
yd = None
#O intervalo da solução como um dicionário
intervalo = None

#O valor de y(0)
y0 = None

#O valor de h
h = None

y,x = symbols('y x')
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
	global arqEntrada, yd, intervalo, y0, h

	intervalo = {}

	#Lendo a função
	yd = eval(arqEntrada.readline())

	#Lendo \n
	arqEntrada.readline()

	y0 = float(arqEntrada.readline())

	#Lendo \n
	arqEntrada.readline()

	#Lendo o intervalo de integração
	intervalo['inicio'] = float(arqEntrada.readline())
	intervalo['fim'] = float(arqEntrada.readline())

	#Lendo \n
	arqEntrada.readline()

	#Lendo a base do sub-espaço
	h = float(arqEntrada.readline())

	#Lendo \n
	arqEntrada.readline()

	linha = arqEntrada.readline()

	return linha

"""
	Método
	yi+1 = yi+ (1/6)(k1 + 2*k2 + 2*k3 + k4)*h
	k1 = f(xi,yi)
	k2 = f(xi + (1/2)*h, yi + (1/2)*h*k1)
	k3 = f(xi + (1/2)*h, yi + (1/2)*k2*h)
	k4 = f(xi + h, yi + k3*h)

"""

def metodoRungeKutta4(f, yi, intervalo, h):
	xi = 0
	k1 = k2 = k3 = k4 = f
	while(xi < intervalo['fim']):
		#Calculando k1
		k1_val = k1.subs(x, xi)
		k1_val = k1_val.subs(y, yi)

		#Calculando k2
		k2_val = k2.subs(x, (xi + (0.5)*h))
		k2_val = k2_val.subs(y, yi + (0.5)*h*k1_val)

		#Calculando k3
		k3_val = k3.subs(x, xi + (0.5)*h)
		k3_val = k3_val.subs(y, yi + (0.5)*k2_val*h)

		#Calculando k4
		k4_val = k4.subs(x, xi + h)
		k4_val = k4_val.subs(y, yi + k3_val*h)

		#Atualizando o yi
		yi = yi + (1/6)*(k1_val + 2*k2_val + 2*k3_val + k4_val)*h

		#Atualizando o xi
		xi = round(xi + h, 2)

	#Aproximando o valor em 3 casas decimais
	yi = round(yi, 3)

	return yi
	

def main():
	global arqSaida, yd, intervalo, y0, h

	#Abrindo os arquivos de entrada e saida
	abrirArquivos()

	while(True):
		fim = lerArquivo()

		#Aplicando o método
		resultado = metodoRungeKutta4(yd, y0, intervalo, h)

		#Imprimindo no arquivo de saida
		arqSaida.write("\nResultado = ")
		arqSaida.write(str(resultado))
		arqSaida.write("\n")

		if(fim == ''):
			break
	#Fechando arquivos
	fecharArquivos()
	
main()
