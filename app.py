import streamlit as st

# Importe as funções dos seus arquivos existentes
# (Certifique-se de que os nomes das funções nos arquivos correspondem a estes)
from quickSort import quick_sort  # Ajuste o nome da função se necessário
from merge_sort import merge_sort
from Insertion_Sort import insertion_sort

st.set_page_config(
    page_title="Visualizador de Ordenação", page_icon="⚡", layout="centered"
)

st.title("Comparador de Algoritmos de Ordenação")
st.write(
    "Insira uma sequência de números para testar os algoritmos implementados"
    " no seu projeto."
)

# Sidebar para escolha do algoritmo
st.sidebar.header("Painel de Controle")
algoritmo = st.sidebar.selectbox(
    "Escolha o Algoritmo", ["Quick Sort", "Merge Sort", "Insertion Sort"]
)

# Entrada de dados do usuário
entrada = st.text_input(
    "Digite os números separados por vírgula:", "10, 3, 5, 1, 8, 2, 7"
)

if st.button("Executar Ordenação"):
  try:
    # Converte o texto digitado em uma lista de números inteiros
    vetor = [int(x.strip()) for x in entrada.split(",")]

    st.info(f"**Vetor Original:** {vetor}")

    # Chama o algoritmo selecionado
    if algoritmo == "Quick Sort":
      resultado = quick_sort(vetor)
    elif algoritmo == "Merge Sort":
      resultado = merge_sort(vetor)
    else:
      resultado = insertion_sort(vetor)

    st.success(f"**Vetor Ordenado:** {resultado}")

  except ValueError:
    st.error(
        "Por favor, digite apenas números válidos separados por vírgula (ex:"
        " 5, 2, 8)."
    )
  except Exception as e:
    st.error(
        f"Erro ao executar o algoritmo. Verifique o retorno da função: {e}"
    )