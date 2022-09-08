op = input('Selecione um tipo de operação \n + para soma: \n - para subtração: \n * para multiplicação: \n / para divisão: \n // para divisão inteira: ' )


if op == "+":
    n1 = input('Digite um valor: ')
    n2 = input('Digite outro valor: ')
    resultado = int(n1) + int(n2)
    print(f'O resultado dessa soma e {resultado}')
elif op == "-":
    n1 = input('Digite um valor: ')
    n2 = input('Digite outro valor: ')
    resultado = int(n1) - int(n2)
    print(f'O resultado dessa subtração e {resultado}')
elif op == "*":
    n1 = input('Digite um valor: ')
    n2 = input('Digite outro valor: ')
    resultado = int(n1) * int(n2)
    print(f'O resultado dessa multiplicação e {resultado}')
elif op == "/":
    n1 = input('Digite um valor: ')
    n2 = input('Digite outro valor: ')
    resultado = int(n1) / int(n2)
    print(f'O resultado dessa divisão e {resultado}')
elif op == "//":
    n1 = input('Digite um valor: ')
    n2 = input('Digite outro valor: ')
    resultado = int(n1) / int(n2)
    print(f'O resultado dessa divisão inteira e {resultado}')
