print("Calculadora")
input("Pressione Enter para continuar...")

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
except ValueError:
    print("Entrada inválida: por favor digite números.")
    raise SystemExit(1)

operacao = input("Digite a operação (+, -, /, *): ").strip()
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "/":
    if num2 == 0:
        print("Erro: divisão por zero.")
        raise SystemExit(1)
    resultado = num1 / num2
elif operacao == "*":
    resultado = num1 * num2
else:
    print("Operação inválida.")
    raise SystemExit(1)

print("O resultado é:", resultado)