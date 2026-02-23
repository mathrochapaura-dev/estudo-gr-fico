import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="Mentor WINFUT", layout="wide")
st.title("📊 Mentor WINFUT - Estudo Noturno")

api_key = st.sidebar.text_input("Cole sua Gemini API Key aqui", type="password")

if api_key:
    try:
        # FORÇANDO A VERSÃO ESTÁVEL v1 NA CONFIGURAÇÃO
        genai.configure(api_key=api_key, transport='rest')
        
        model = genai.GenerativeModel('gemini-1.5-flash')

        uploaded_files = st.file_uploader("Suba seus prints", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'])

        if st.button("🚀 Analisar Agora"):
            if uploaded_files:
                with st.spinner("Analisando gráficos..."):
                    prompt = "Analise o Price Action (Cassius Andrei) nestes gráficos de WINFUT. Identifique suportes, resistências e Traps."
                    conteudo = [prompt]
                    for f in uploaded_files:
                        img = Image.open(f)
                        conteudo.append(img)
                    
                    response = model.generate_content(conteudo)
                    st.markdown("---")
                    st.write(response.text)
            else:
                st.warning("Selecione os prints primeiro.")
    except Exception as e:
        st.error(f"Erro: {e}")
else:
    st.info("Insira sua chave para começar.")

