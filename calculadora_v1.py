# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!


print("\n******************* Python Calculator *******************")

# FUNCOES CALCULADORA
def somar (num1,num2):    
    soma = num1 + num2
    return soma

def subtrair (num1,num2):   
    subtracao = num1 - num2
    return subtracao

def multiplicar (num1,num2):    
    multiplicacao = num1 * num2
    return multiplicacao

def dividir (num1,num2):    
    divisao = num1 / num2
    if num1 == 0 or num2 == 0:
        try:
            print("\nImpossível essa Divisão!")             
        finally:
            divisao
    return divisao
            
    
 
# ENTRADA USUARIO
select_operation = int(input("SELECIONE A OPERAÇÃO DESEJADA:\n\n0- SAIR\n\n1- SOMA\n2- SUBTRAÇÃO\n3- MULTIPLICAÇÃO\n4- DIVISÃO\n\n=> "))


while select_operation > 0 and select_operation < 5:

    num1 = float(input("\nInforme o primeiro número: "))
    num2 = float(input("Informe o segundo número: "))
        
    if select_operation == 1:        
        print(f"\nResultado da Soma: {somar(num1,num2)}\n\n")
    elif select_operation == 2:
        print(f"\nResultado da Subtração: {subtrair(num1,num2)}\n\n")
    elif select_operation == 3:
        print(f"\nResultado da Multiplicação: {multiplicar(num1,num2)}\n\n")
    elif select_operation == 4:    
        print(f"\nResultado da Divisão: {dividir(num1,num2)}\n\n")
    else:
        print("Operação Inválida!")
        break
    
    select_operation = int(input("SELECIONE A OPERAÇÃO DESEJADA:\n\n0- SAIR\n\n1- SOMA\n2- SUBTRAÇÃO\n3- MULTIPLICAÇÃO\n4- DIVISÃO\n\n=> "))
    

    

