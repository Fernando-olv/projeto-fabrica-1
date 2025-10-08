import streamlit as st

def avaliar_situacao(media):
    if media >= 7.0:
        return "Aprovado(a) ✅"
    elif media >= 5.0:
        return "Recuperação ⚠️"
    else:
        return "Reprovado(a) ❌"



st.title("Calculadora de Média Escolar")
st.image("https://diariodorio.com/wp-content/uploads/2016/01/Material_escolar-1.jpg")
nome = st.text_input("Nome do estudante")
quantidade = st.number_input("Quantidade de notas", min_value=1, step=1)



notas = []
for i in range(int(quantidade)):
    nota = st.number_input(f"Nota {i+1}", min_value=0.0, max_value=10.0)
    notas.append(nota)

if st.button("Calcular média"):
    media = sum(notas)/len(notas)
    situacao = avaliar_situacao(media)
    st.success(f"Média: {media:.2f} — Situação: {situacao}")