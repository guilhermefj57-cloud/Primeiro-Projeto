print "Calculadora "
input("Pressione Enter para continuar...")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, /, *): ")
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "/":
    resultado = num1 / num2
elif operacao == "*":
    resultado = num1 * num2
print("O resultado é: ", resultado)