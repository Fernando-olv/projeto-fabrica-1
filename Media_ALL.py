nota1 = float(input("Digite a primeira nota (0 a 10): "))

nota2 = float(input("Digite a segunda nota (0 a 10): "))

nota3 = float(input("Digite a terceira nota (0 a 10): "))

nota4 = float(input("Digite a quarta nota (0 a 10): "))


media = (nota1 + nota2 + nota3 + nota4) / 4


print(f"\nMédia final: {media:.2f}")
if media >= 7.0:
    print("Aprovado ✅")
elif media >= 5.0:
    print("Recuperaçao ⚠️")
else:
    print("Reprovado ❌")
