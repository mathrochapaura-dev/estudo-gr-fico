import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

# Força o uso da versão estável da API
os.environ["GOOGLE_API_USE_MTLS_ENDPOINT"] = "never"

st.set_page_config(page_title="Mentor WINFUT", layout="wide")
st.title("📊 Mentor WINFUT - Estudo Noturno")

api_key = st.sidebar.text_input("Cole sua Gemini API Key aqui", type="password")

PROMPT = "Analise o Price Action (Cassius Andrei) nestes gráficos de WINFUT. Identifique suportes, resistências, Traps e dê o Plano de Voo."

if api_key:
    try:
        genai.configure(api_key=api_key)
        # Nome do modelo corrigido para evitar erro 404
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")

        uploaded_files = st.file_uploader("Suba seus prints", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'])

        if st.button("🚀 Analisar Agora"):
            if uploaded_files:
                with st.spinner("Analisando..."):
                    conteudo = [PROMPT]
                    for f in uploaded_files:
                        img = Image.open(f)
                        conteudo.append(img)
                    
                    response = model.generate_content(conteudo)
                    st.markdown("---")
                    st.write(response.text)
            else:
                st.warning("Selecione os prints primeiro.")
    except Exception as e:
        st.error(f"Erro técnico: {e}")
else:
    st.info("Insira sua chave para começar.")

