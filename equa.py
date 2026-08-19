import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Equação do 1º Grau",
    page_icon="📈",
    layout="centered"
)

# ============================================================
# ESTILO DA PÁGINA
# ============================================================

st.markdown("""
<style>

    /* Fundo principal */
    .stApp {
        background-color: #ffe6f0;
    }

    /* Área principal */
    .main {
        background-color: #ffe6f0;
    }

    /* Título */
    h1 {
        color: #c2185b;
        text-align: center;
    }

    h2, h3 {
        color: #ad1457;
    }

    /* Textos */
    p, label {
        color: #5c1640 !important;
    }

    /* Caixa dos números */
    div[data-baseweb="input"] {
        background-color: #fff5f8;
        border-radius: 10px;
        border: 1px solid #f48fb1;
    }

    /* Botão */
    .stButton > button {
        background-color: #e91e63;
        color: white;
        border: none;
        border-radius: 10px;
        font-size: 18px;
        font-weight: bold;
        padding: 10px;
    }

    .stButton > button:hover {
        background-color: #c2185b;
        color: white;
    }

    /* Caixa de sucesso */
    div[data-testid="stAlert"] {
        border-radius: 10px;
    }

    /* Rodapé */
    .rodape {
        text-align: center;
        color: #ad1457;
        font-size: 14px;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# CAMINHOS
# ============================================================

PASTA_APP = Path(__file__).parent

CAMINHO_LOGO = PASTA_APP / "mat.jpeg.jpeg"


# ============================================================
# LOGO / IMAGEM
# ============================================================

if CAMINHO_LOGO.exists():

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image(
            str(CAMINHO_LOGO),
            use_container_width=True
        )

else:
    st.warning(
        "A imagem mat.jpeg não foi encontrada. ⚠️"
    )


# ============================================================
# TÍTULO
# ============================================================

st.title("Equação do 1º Grau 📈")

st.write("### Equação no formato:")

st.latex(r"ax + b = 0")


# ============================================================
# ENTRADA DOS VALORES
# ============================================================

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


# ============================================================
# BOTÃO CALCULAR
# ============================================================

if st.button(
    "Calcular",
    use_container_width=True
):

    # --------------------------------------------------------
    # CASO a = 0
    # --------------------------------------------------------

    if a == 0:

        # 0x + 0 = 0
        if b == 0:

            st.warning(
                "A equação possui infinitas soluções."
            )

        # 0x + b = 0
        else:

            st.error(
                "A equação não possui solução."
            )


    # --------------------------------------------------------
    # CASO a ≠ 0
    # --------------------------------------------------------

    else:

        # Cálculo da raiz
        x_raiz = -b / a


        # ====================================================
        # RESULTADO
        # ====================================================

        st.subheader("Resultado ✅")

        st.write("A raiz da equação é:")

        st.success(
            f"x = {x_raiz:.2f}"
        )


        # ====================================================
        # EQUAÇÃO
        # ====================================================

        st.subheader("Equação")

        if b >= 0:

            st.latex(
                f"{a}x + {b} = 0"
            )

        else:

            st.latex(
                f"{a}x - {abs(b)} = 0"
            )


        # ====================================================
        # RESOLUÇÃO
        # ====================================================

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


        # ====================================================
        # GRÁFICO
        # ====================================================

        st.subheader("Gráfico da função 📊")

        x = np.linspace(
            x_raiz - 10,
            x_raiz + 10,
            500
        )

        y = a * x + b


        # Criação do gráfico
        fig, ax = plt.subplots(
            figsize=(8, 5)
        )

        # Fundo do gráfico
        fig.patch.set_facecolor("#fff0f5")
        ax.set_facecolor("#fff8fa")


        # Linha da função
        ax.plot(
            x,
            y,
            color="#e91e63",
            linewidth=2.5,
            label=f"y = {a}x + {b}"
        )


        # Eixo X
        ax.axhline(
            y=0,
            color="#555555",
            linewidth=1
        )


        # Eixo Y
        ax.axvline(
            x=0,
            color="#555555",
            linewidth=1
        )


        # Ponto da raiz
        ax.scatter(
            [x_raiz],
            [0],
            color="#880e4f",
            s=100,
            zorder=5,
            label=f"Raiz x = {x_raiz:.2f}"
        )


        # Configurações
        ax.set_xlabel(
            "x",
            color="#5c1640"
        )

        ax.set_ylabel(
            "y",
            color="#5c1640"
        )

        ax.set_title(
            "Gráfico da Função do 1º Grau",
            color="#c2185b"
        )

        ax.grid(
            True,
            alpha=0.3
        )

        ax.legend()


        # Exibe o gráfico
        st.pyplot(fig)

        # Fecha a figura
        plt.close(fig)


# ============================================================
# RODAPÉ
# ============================================================

st.divider()

st.markdown(
    '<div class="rodape">Calculadora de Equação do 1º Grau 📚💕</div>',
    unsafe_allow_html=True
)
