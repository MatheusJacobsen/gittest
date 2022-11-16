# Nome: Matheus Marques Jacobsen
# Numero USP: 10312403
# Atividade 5 da Disciplina Desenvolvimento de Software para Sistemas Embarcados com Sistemas Operacionais
# SEL0456

# Função Fatorial (recursiva)
def fact(x):
    return x * fact(x - 1) if x > 1 else 1

# Sequência de Fibonacci
def fib(x):
    return fib(x - 1) + fib(x - 2) if x > 1 else 1 if x == 1 else 0

# Leitura de Arquivo de Entrada
with open('C:\Users\mathe\gittest\gittest\wrong_data', 'r') as inputFile:
    lines = inputFile.readlines()

firstNumber = []
secondNumber = []
thirdNumber = []
for line in lines:
    if ((len(line) > 1) and line != lines[0]):
        splitted = line.split(' ')
        firstNumber.append(int(splitted[0]))
        secondNumber.append(int(splitted[1]))
        thirdNumber.append(int(splitted[2].split('\n')[0]))

def testAnswers():
    for i in range(len(firstNumber)):
        assert fib(firstNumber[i]) == thirdNumber[i] \
            and fact(firstNumber[i]) == secondNumber[i], "Error on line {} (starting on 1 and excluding header and empty lines)".format(i + 1)