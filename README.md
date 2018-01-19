# Explicação
Cada diretório contém implementações de diferentes métodos matemáticos em Python, e também um relatório para explanar como estes métodos foram implementados.

# Parte do Relatório
## Linguagem(ns) Escolhida(s) e justificativas
A linguagem escolhida foi o Python, pois além de ser uma linguagem em que o autor deste relatório já é familiarizado, existem algumas bibliotecas para cálculos matemáticos e manipulação de funções que já estão implementadas para se utilizar nesta linguagem. A versão do python utilizada foi a versão 3.5.3. O Sistema Operacional usado para implementar os métodos foi o Linux distribuição Ubuntu 17.04.

## Especificações Arquivo de Entrada
### Biblioteca usada:
Para todos os métodos foi necessário usar uma biblioteca chamada sympy. Para instalar esta biblioteca no Python3, foi utilizado o seguinte comando no terminal Linux: $ sudo pip3 install sympy. Foi preferível usar esta biblioteca para todos os métodos porque além de implementar funções para cálculos matemáticos (exponencial, seno, cosseno...), também implementa manipulação de funções e equações (f(x) = x + y + z, x + y = 1...). Por isso foi aberta esta nova sessão para explicar como são representadas as funções matemáticas a partir desta biblioteca.

Também foi utilizada em todos os métodos uma biblioteca chamada sys. Esta biblioteca permite usar argumentos em python, e ela foi usada para inserir como argumento do programa o caminho do arquivo de entrada.

Para poder executar qualquer método, deve-se digitar pyhon3 (ou python, caso a versão 3 esteja configurada como padrão na máquina), o nome do arquivo .py e depois o nome do arquivo de entrada como parâmetro.

> $ python3 nomeDoMetodo.py entrada.txt

### Algumas representações
Abaixo se encontram as representações de algumas funções matemáticas que podem ser usadas no arquivo de entrada:
> x² = pow(x, 2) ou x**2;<br>
> Raiz quadrada de x = sqrt(x);<br>
> Seno de x = sin(x);<br>
> Arcoseno de x = asin(x);<br>
> Cosseno de x = cos(x);<br>
> Tangente de x = tan(x);<br>
> Número de Euler (e) elevado a x = exp(x);<br>
> Log de x na base y = log(x, y);<br>
> pi é uma constante já definida (3,1415...).