import streamlit as st
from src.engine import MissionEngine

st.set_page_config(page_title="Mission Control AI", layout="wide")
st.title("🚀 Mission Control AI - ConnectSat")

engine = MissionEngine()

st.sidebar.header("Telemetria Atual")
if st.sidebar.button("Atualizar Telemetria"):
    st.session_state.telemetria = engine.status_snapshot()

if "telemetria" in st.session_state:
    st.sidebar.text(st.session_state.telemetria)

pergunta = st.text_area("Faça sua pergunta ao Mission Control:", height=100)

if st.button("Enviar para IA"):
    if pergunta:
        with st.spinner("Analisando..."):
            resposta = engine.analyze(pergunta)
        st.markdown("### Resposta:")
        st.write(resposta)
    else:
        st.warning("Digite uma pergunta.")