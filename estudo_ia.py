import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="Mentor WINFUT", layout="wide")
st.title("📊 Mentor WINFUT - Estudo Noturno")

api_key = st.sidebar.text_input("Cole sua Gemini API Key aqui", type="password")

if api_key:
    try:
        # O SEGREDO: Forçamos o uso do transporte REST para evitar o erro 404 da v1beta
        genai.configure(api_key=api_key, transport='rest')
        
        # Usamos o nome oficial sem prefixos que causam erro
        model = genai.GenerativeModel('gemini-1.5-flash')

        uploaded_files = st.file_uploader("Suba seus prints", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'])

        if st.button("🚀 Analisar Agora"):
            if uploaded_files:
                with st.spinner("IA processando seus gráficos..."):
                    prompt = "Você é um auditor de Price Action (Cassius Andrei). Analise estes prints de WINFUT, identifique suportes, resistências e possíveis Traps."
                    conteudo = [prompt]
                    for f in uploaded_files:
                        img = Image.open(f)
                        conteudo.append(img)
                    
                    response = model.generate_content(conteudo)
                    st.markdown("---")
                    st.write(response.text)
            else:
                st.warning("Cadê os prints? Sobe os arquivos primeiro!")
    except Exception as e:
        st.error(f"Erro técnico: {e}")
else:
    st.info("Insira sua chave para liberar o acesso gratuito.")


