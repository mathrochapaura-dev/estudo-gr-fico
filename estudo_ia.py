import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="Mentor WINFUT", layout="wide")
st.title("📊 Mentor WINFUT - Estudo Noturno")

api_key = st.sidebar.text_input("Cole sua Gemini API Key aqui", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # USANDO O FORMATO SIMPLIFICADO QUE O GOOGLE EXIGE EM 2026
        model = genai.GenerativeModel('gemini-1.5-flash')

        uploaded_files = st.file_uploader("Suba seus prints", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'])

        if st.button("🚀 Analisar Agora"):
            if uploaded_files:
                with st.spinner("IA processando..."):
                    # Instrução direta para a IA
                    prompt = "Analise o Price Action (Cassius Andrei) nestes prints de WINFUT. Identifique suportes, resistências e Traps."
                    conteudo = [prompt]
                    for f in uploaded_files:
                        img = Image.open(f)
                        conteudo.append(img)
                    
                    response = model.generate_content(conteudo)
                    st.markdown("---")
                    st.write(response.text)
            else:
                st.warning("Selecione os arquivos primeiro.")
    except Exception as e:
        st.error(f"Erro na conexão: {e}")
else:
    st.info("Insira sua chave para começar.")


