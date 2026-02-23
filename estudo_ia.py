import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="Mentor WINFUT", layout="wide")
st.title("📊 Mentor WINFUT - Estudo Noturno")

api_key = st.sidebar.text_input("Cole sua Gemini API Key aqui", type="password")

PROMPT = "Analise estes gráficos de WINFUT (Price Action). Identifique suportes, resistências, potenciais Traps e defina o Plano de Voo (Alvo e Stop) conforme o método Cassius Andrei."

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # Esta linha força o sistema a não usar a versão 'beta' que está dando erro
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

        uploaded_files = st.file_uploader("Suba seus prints", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'])

        if st.button("🚀 Analisar Agora"):
            if uploaded_files:
                with st.spinner("IA processando..."):
                    conteudo = [PROMPT]
                    for f in uploaded_files:
                        img = Image.open(f)
                        conteudo.append(img)
                    
                    # Chamada direta e simplificada
                    response = model.generate_content(conteudo)
                    
                    st.markdown("---")
                    st.markdown("### 📋 Resultado da Auditoria:")
                    st.write(response.text)
            else:
                st.warning("Selecione os prints antes de analisar.")
    except Exception as e:
        st.error(f"Erro detectado: {e}")
else:

    st.info("Insira sua chave para liberar o acesso gratuito.")
