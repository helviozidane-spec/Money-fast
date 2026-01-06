import streamlit as st

# -----------------------------
# CONFIGURAÇÃO GERAL
# -----------------------------
st.set_page_config(
    page_title="BankCard Simulator",
    layout="wide"
)

st.markdown("""
<style>
    .block-container {
        padding-top: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# CABEÇALHO
# -----------------------------
st.title("🏦 Money Fast by HZ")
st.caption("Simulador de taxas bancárias para cartões Visa (uso educativo e financeiro)")

st.divider()

# -----------------------------
# INPUTS
# -----------------------------
st.subheader("📥 Dados da Simulação")

col1, col2 = st.columns(2)

with col1:
    valor_plafon = st.number_input(
        "Valor a carregar no cartão (Kz)",
        min_value=0.0,
        step=1000.0
    )

with col2:
    cambio = st.number_input(
        "Câmbio do dia (Kz / €)",
        min_value=1.0,
        step=1.0
    )

if valor_plafon > 0 and cambio > 0:

    st.divider()

    # -----------------------------
    # CARREGAMENTO
    # -----------------------------
    st.subheader("💳 Carregamento do Cartão")

    col3, col4 = st.columns(2)

    taxa_carregamento = valor_plafon * 0.02
    iva_carregamento = taxa_carregamento * 0.14
    total_taxas_carregamento = taxa_carregamento + iva_carregamento
    valor_necessario_conta = valor_plafon + total_taxas_carregamento

    with col3:
        st.metric("Taxa 2%", f"{taxa_carregamento:,.2f} Kz")
        st.metric("IVA (14%)", f"{iva_carregamento:,.2f} Kz")

    with col4:
        st.metric("Total de Taxas", f"{total_taxas_carregamento:,.2f} Kz")
        st.metric("Valor necessário na conta", f"{valor_necessario_conta:,.2f} Kz")

    st.divider()

    # -----------------------------
    # USO EM EURO
    # -----------------------------
    st.subheader("💶 Uso do Cartão em Euro")

    taxa_6 = valor_plafon * 0.06          # sem IVA
    taxa_3 = valor_plafon * 0.03          # com IVA
    iva_3 = taxa_3 * 0.14

    total_descontos = taxa_6 + taxa_3 + iva_3
    valor_liquido_kz = valor_plafon - total_descontos
    valor_liquido_euro = valor_liquido_kz / cambio

    col5, col6, col7 = st.columns(3)

    with col5:
        st.metric("Taxa 6% (sem IVA)", f"{taxa_6:,.2f} Kz")

    with col6:
        st.metric("Taxa 3%", f"{taxa_3:,.2f} Kz")
        st.metric("IVA sobre 3%", f"{iva_3:,.2f} Kz")

    with col7:
        st.metric("Valor líquido (Kz)", f"{valor_liquido_kz:,.2f} Kz")
        st.metric("Valor disponível (€)", f"{valor_liquido_euro:,.2f} €")

    st.divider()

# -----------------------------
# DISCLAIMER
# -----------------------------
st.caption("""
⚠️ **Aviso Legal:**  
Este simulador é meramente informativo. As taxas podem variar conforme o banco,
o tipo de cartão e atualizações do preçário oficial.
Confirme sempre com o seu banco antes de realizar operações financeiras.
""")

