nome = input("Insira aqui o nome do aluno: ")

notas = []

quantidade_notas = int(input("Quantas notas serão necessárias para calcular? "))
for n in range(quantidade_notas):
    nota = float(input(f"Insira a {n + 1}a nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)

#nota1 = float(input('Insira a primeira nota: '))
#nota2 = float(input('Insira a segunda nota: '))
#nota3 = float(input('Insira a terceira nota: '))
#nota4 = float(input('Insira a quarta nota: '))
#media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print(f"A média do aluno é igual a {media:.2f}.\nAprovado!")
elif media >=5 and media < 7:
    print(f"A média do aluno é igual a {media:.2f}.\nEm recuperação!")
else:
    print(f"A média do aluno é igual a {media:.2f}.\nReprovado!")