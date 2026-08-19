import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Configuração da página
st.set_page_config(
    page_title="Equação do 1º Grau",
    page_icon="📈",
    layout="centered"
)

# Caminho da pasta do aplicativo
PASTA_APP = Path(__file__).parent

# Caminho da imagem
CAMINHO_LOGO = PASTA_APP / "mat.jpeg"

# Exibe a imagem, se existir
if CAMINHO_LOGO.exists():
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image(
            str(CAMINHO_LOGO),
            use_container_width=True
        )
else:
    st.warning("A imagem mat.jpeg não foi encontrada. ⚠️")


# Título
st.title("Equação do 1º Grau 📈")

st.write("Equação no formato:")

st.latex(r"ax + b = 0")


# Entrada dos valores
a = st.number_input(
    "Digite o valor de a",
    value=1,
    step=1
)

b = st.number_input(
    "Digite o valor de b",
    value=0,
    step=1
)


# Botão calcular
if st.button("Calcular", use_container_width=True):

    # Caso a seja igual a zero
    if a == 0:

        # 0x + 0 = 0
        if b == 0:
            st.warning(
                "A equação possui infinitas soluções."
            )

        # 0x + b = 0, com b diferente de zero
        else:
            st.error(
                "A equação não possui solução."
            )

    # Caso a seja diferente de zero
    else:

        # Cálculo da raiz
        x_raiz = -b / a

        # Resultado
        st.subheader("Resultado ✅")

        st.write("A raiz da equação é:")

        st.success(
            f"x = {x_raiz:.2f}"
        )

        # Equação
        st.subheader("Equação")

        if b >= 0:
            st.latex(
                f"{a}x + {b} = 0"
            )
        else:
            st.latex(
                f"{a}x - {abs(b)} = 0"
            )

        # Resolução
        st.subheader("Resolução")

        if b >= 0:
            st.latex(
                f"{a}x + {b} = 0"
            )
        else:
            st.latex(
                f"{a}x - {abs(b)} = 0"
            )

        st.latex(
            f"{a}x = {-b}"
        )

        st.latex(
            rf"x = \frac{{{-b}}}{{{a}}}"
        )

        st.latex(
            f"x = {x_raiz:.2f}"
        )

        # Gráfico
        st.subheader("Gráfico da função 📊")

        x = np.linspace(
            x_raiz - 10,
            x_raiz + 10,
            500
        )

        y = a * x + b

        fig, ax = plt.subplots(
            figsize=(8, 5)
        )

        # Linha da função
        ax.plot(
            x,
            y,
            linewidth=2,
            label=f"y = {a}x + {b}"
        )

        # Eixos
        ax.axhline(
            y=0,
            color="black",
            linewidth=1
        )

        ax.axvline(
            x=0,
            color="black",
            linewidth=1
        )

        # Ponto da raiz
        ax.scatter(
            [x_raiz],
            [0],
            color="red",
            s=100,
            zorder=5,
            label=f"Raiz x = {x_raiz:.2f}"
        )

        # Configurações do gráfico
        ax.set_xlabel("x")
        ax.set_ylabel("y")

        ax.set_title(
            "Gráfico da Função do 1º Grau"
        )

        ax.grid(True)
        ax.legend()

        # Exibe o gráfico
        st.pyplot(fig)

        # Fecha a figura
        plt.close(fig)


# Rodapé
st.divider()

st.caption(
    "Calculadora de Equação do 1º Grau 📚"
)

