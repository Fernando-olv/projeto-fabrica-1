def solicitar_nota(numero_bimestre):
    while True:
        try:
            nota = float(input(f"Digite a {numero_bimestre}ª nota (0 a 10): "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("❌ Valor inválido. Digite uma nota entre 0 e 10.")
        except ValueError:
            print("❌ Entrada inválida. Digite um número decimal.")

def calcular_media(notas):
    return sum(notas) / len(notas)

def avaliar_situacao(media):
    if media >= 7.0:
        return "Aprovado(a) ✅"
    elif media >= 5.0:
        return "Recuperação ⚠️"
    else:
        return "Reprovado(a) ❌"

def exibir_resultado(media, situacao):
    print(f"\nMédia: {media:.2f} — Situação: {situacao}")

def main():
    notas = [solicitar_nota(i) for i in range(1, 5)]
    media = calcular_media(notas)
    situacao = avaliar_situacao(media)
    exibir_resultado(media, situacao)

if __name__ == "__main__":
    main()